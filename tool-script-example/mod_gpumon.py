# Copyright 2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#  
#  or in the "license" file accompanying this file. This file is distributed 
#  on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either 
#  express or implied. See the License for the specific language governing 
#  permissions and limitations under the License.


import urllib2
import boto3
from pynvml import *
from datetime import datetime
from time import sleep

### CHOOSE REGION ####
EC2_REGION = 'us-east-1'

###CHOOSE NAMESPACE PARMETERS HERE###
my_NameSpace = 'CP4CC_GPU'

### CHOOSE PUSH INTERVAL ####
sleep_interval = 10

### CHOOSE STORAGE RESOLUTION (BETWEEN 1-60) ####
store_reso = 60

#Instance information
BASE_URL = 'http://169.254.169.254/latest/meta-data/'
INSTANCE_ID = urllib2.urlopen(BASE_URL + 'instance-id').read()
IMAGE_ID = urllib2.urlopen(BASE_URL + 'ami-id').read()
INSTANCE_TYPE = urllib2.urlopen(BASE_URL + 'instance-type').read()
INSTANCE_AZ = urllib2.urlopen(BASE_URL + 'placement/availability-zone').read()
EC2_REGION = INSTANCE_AZ[:-1]

TIMESTAMP = datetime.now().strftime('%Y-%m-%dT%H')
TMP_FILE = '/tmp/GPU_TEMP'
TMP_FILE_SAVED = TMP_FILE + TIMESTAMP

# Create CloudWatch client
cloudwatch = boto3.client('cloudwatch', region_name=EC2_REGION)


# Flag to push to CloudWatch
PUSH_TO_CW = True

def getPowerDraw(handle):
    try:
        powDraw = nvmlDeviceGetPowerUsage(handle) / 1000.0
        powDrawStr = '%.2f' % powDraw
    except NVMLError as err:
        powDrawStr = handleError(err)
        PUSH_TO_CW = False
    return powDrawStr

def getTemp(handle):
    try:
        temp = str(nvmlDeviceGetTemperature(handle, NVML_TEMPERATURE_GPU))
    except NVMLError as err:
        temp = handleError(err)
        PUSH_TO_CW = False
    return temp

def getUtilization(handle):
    try:
        util = nvmlDeviceGetUtilizationRates(handle)
        gpu_util = str(util.gpu)
     #   mem_util = str(util.memory)
        meminfo = nvmlDeviceGetMemoryInfo(handle)
        mem_used = str(meminfo.used / 1024. ** 3)
    except NVMLError as err:
        error = handleError(err)
        gpu_util = error
     #   mem_util = error
        PUSH_TO_CW = False
    return util, gpu_util, mem_used

def logResults(i, util, gpu_util, mem_used, powDrawStr, temp):
    try:
        gpu_logs = open(TMP_FILE_SAVED, 'a+')
        writeString = str(i) + ',' + gpu_util + ',' + mem_used + ',' + powDrawStr + ',' + temp + '\n'
        if float(gpu_util) > 0:
            print writeString
        gpu_logs.write(writeString)
    except:
        print("Error writing to file ", gpu_logs)
    finally:
        gpu_logs.close()
    if (PUSH_TO_CW):
        MY_DIMENSIONS=[
                    {
                        'Name': 'InstanceId',
                        'Value': INSTANCE_ID
                    },
                    {
                        'Name': 'ImageId',
                        'Value': IMAGE_ID
                    },
                    {
                        'Name': 'InstanceType',
                        'Value': INSTANCE_TYPE
                    },
                    {
                        'Name': 'GPUNumber',
                        'Value': str(i)
                    }
                ]
        cloudwatch.put_metric_data(
            MetricData=[
                {
                    'MetricName': 'GPU Usage',
                    'Dimensions': MY_DIMENSIONS,
                    'Unit': 'Percent',
                    'StorageResolution': store_reso,
                    'Value': util.gpu
                },
                {
                    'MetricName': 'Memory Usage',
                    'Dimensions': MY_DIMENSIONS,
                    'Unit': 'Gigabytes',
                    'StorageResolution': store_reso,
                    'Value': float(mem_used)
                },
        ],
            Namespace=my_NameSpace
        )

def logResultsAvg(gpu_util_avg, mem_used_avg):
    try:
        gpu_logs = open(TMP_FILE_SAVED, 'a+')
        writeString = 'avg:' + str(gpu_util_avg) + ',' + str(mem_used_avg) + '\n'
        if float(gpu_util_avg) > 0:
            print writeString
        gpu_logs.write(writeString)
    except:
        print("Error writing to file ", gpu_logs)
    finally:
        gpu_logs.close()
    if (PUSH_TO_CW):
        MY_DIMENSIONS=[
                    {
                        'Name': 'InstanceId',
                        'Value': INSTANCE_ID
                    },
                    {
                        'Name': 'ImageId',
                        'Value': IMAGE_ID
                    },
                    {
                        'Name': 'InstanceType',
                        'Value': INSTANCE_TYPE
                    },
                ]
        cloudwatch.put_metric_data(
            MetricData=[
                {
                    'MetricName': 'Avg GPU Usage',
                    'Dimensions': MY_DIMENSIONS,
                    'Unit': 'Percent',
                    'StorageResolution': store_reso,
                    'Value': gpu_util_avg
                },
                {
                    'MetricName': 'Avg Memory Usage',
                    'Dimensions': MY_DIMENSIONS,
                    'Unit': 'Gigabytes',
                    'StorageResolution': store_reso,
                    'Value': mem_used_avg
                },
        ],
            Namespace=my_NameSpace
        )


nvmlInit()
deviceCount = nvmlDeviceGetCount()

def main():
    try:
        while True:
            PUSH_TO_CW = True
            avg_gpu_util = 0.0
            avg_mem_used = 0.0
            # Find the metrics for each GPU on instance
            for i in range(deviceCount):
                handle = nvmlDeviceGetHandleByIndex(i)

                powDrawStr = getPowerDraw(handle)
                temp = getTemp(handle)
                util, gpu_util, mem_used = getUtilization(handle)
                logResults(i, util, gpu_util, mem_used, powDrawStr, temp)
                avg_gpu_util += float(gpu_util)
                avg_mem_used += float(mem_used)
            # Next, push avg statistics
            avg_gpu_util /= deviceCount
            avg_mem_used /= deviceCount
            logResultsAvg(avg_gpu_util, avg_mem_used)
            sleep(sleep_interval)

    finally:
        nvmlShutdown()

if __name__=='__main__':
    main()


# run command
# PYTHONPATH=/usr/lib/python2.7/site-packages nohup python avg_mod_gpumon.py > /dev/null &
#

