# swagger_client.MailboxesApi

All URIs are relative to *http://localhost:8088/ari*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mailboxes_get**](MailboxesApi.md#mailboxes_get) | **GET** /mailboxes | List all mailboxes.
[**mailboxes_mailbox_name_delete**](MailboxesApi.md#mailboxes_mailbox_name_delete) | **DELETE** /mailboxes/{mailboxName} | Destroy a mailbox.
[**mailboxes_mailbox_name_get**](MailboxesApi.md#mailboxes_mailbox_name_get) | **GET** /mailboxes/{mailboxName} | Retrieve the current state of a mailbox.
[**mailboxes_mailbox_name_put**](MailboxesApi.md#mailboxes_mailbox_name_put) | **PUT** /mailboxes/{mailboxName} | Change the state of a mailbox. (Note - implicitly creates the mailbox).


# **mailboxes_get**
> list[Mailbox] mailboxes_get()

List all mailboxes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.MailboxesApi(swagger_client.ApiClient(configuration))

try:
    # List all mailboxes.
    api_response = api_instance.mailboxes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailboxesApi->mailboxes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Mailbox]**](Mailbox.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mailboxes_mailbox_name_delete**
> mailboxes_mailbox_name_delete(mailbox_name)

Destroy a mailbox.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.MailboxesApi(swagger_client.ApiClient(configuration))
mailbox_name = 'mailbox_name_example' # str | Name of the mailbox

try:
    # Destroy a mailbox.
    api_instance.mailboxes_mailbox_name_delete(mailbox_name)
except ApiException as e:
    print("Exception when calling MailboxesApi->mailboxes_mailbox_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox_name** | **str**| Name of the mailbox | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mailboxes_mailbox_name_get**
> Mailbox mailboxes_mailbox_name_get(mailbox_name)

Retrieve the current state of a mailbox.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.MailboxesApi(swagger_client.ApiClient(configuration))
mailbox_name = 'mailbox_name_example' # str | Name of the mailbox

try:
    # Retrieve the current state of a mailbox.
    api_response = api_instance.mailboxes_mailbox_name_get(mailbox_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MailboxesApi->mailboxes_mailbox_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox_name** | **str**| Name of the mailbox | 

### Return type

[**Mailbox**](Mailbox.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mailboxes_mailbox_name_put**
> mailboxes_mailbox_name_put(mailbox_name, old_messages, new_messages)

Change the state of a mailbox. (Note - implicitly creates the mailbox).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.MailboxesApi(swagger_client.ApiClient(configuration))
mailbox_name = 'mailbox_name_example' # str | Name of the mailbox
old_messages = 56 # int | Count of old messages in the mailbox
new_messages = 56 # int | Count of new messages in the mailbox

try:
    # Change the state of a mailbox. (Note - implicitly creates the mailbox).
    api_instance.mailboxes_mailbox_name_put(mailbox_name, old_messages, new_messages)
except ApiException as e:
    print("Exception when calling MailboxesApi->mailboxes_mailbox_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mailbox_name** | **str**| Name of the mailbox | 
 **old_messages** | **int**| Count of old messages in the mailbox | 
 **new_messages** | **int**| Count of new messages in the mailbox | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

