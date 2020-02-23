#pip install MeaningCloud-python

import sys
import meaningcloud
import os
import pandas as pd
license_key = '790232bd43fd37faa96753ee499fb6ea'

def getSummarization(text, sentences):
    
    summary = ''
    #print("\tGetting automatic summarization...")
    summarization_response = meaningcloud.SummarizationResponse(meaningcloud.SummarizationRequest(license_key, sentences=sentences, txt=text).sendReq())
    if summarization_response.isSuccessful():
        summary = summarization_response.getSummary()
    else:
        print("\tOops! Request to Summarization was not succesful: (" + summarization_response.getStatusCode() + ') ' + summarization_response.getStatusMsg())

    return summary 


