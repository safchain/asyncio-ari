# swagger_client.AsteriskApi

All URIs are relative to *http://localhost:8088/ari*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asterisk_config_dynamic_config_class_object_type_id_delete**](AsteriskApi.md#asterisk_config_dynamic_config_class_object_type_id_delete) | **DELETE** /asterisk/config/dynamic/{configClass}/{objectType}/{id} | Delete a dynamic configuration object.
[**asterisk_config_dynamic_config_class_object_type_id_get**](AsteriskApi.md#asterisk_config_dynamic_config_class_object_type_id_get) | **GET** /asterisk/config/dynamic/{configClass}/{objectType}/{id} | Retrieve a dynamic configuration object.
[**asterisk_config_dynamic_config_class_object_type_id_put**](AsteriskApi.md#asterisk_config_dynamic_config_class_object_type_id_put) | **PUT** /asterisk/config/dynamic/{configClass}/{objectType}/{id} | Create or update a dynamic configuration object.
[**asterisk_info_get**](AsteriskApi.md#asterisk_info_get) | **GET** /asterisk/info | Gets Asterisk system information.
[**asterisk_logging_get**](AsteriskApi.md#asterisk_logging_get) | **GET** /asterisk/logging | Gets Asterisk log channel information.
[**asterisk_logging_log_channel_name_delete**](AsteriskApi.md#asterisk_logging_log_channel_name_delete) | **DELETE** /asterisk/logging/{logChannelName} | Deletes a log channel.
[**asterisk_logging_log_channel_name_post**](AsteriskApi.md#asterisk_logging_log_channel_name_post) | **POST** /asterisk/logging/{logChannelName} | Adds a log channel.
[**asterisk_logging_log_channel_name_rotate_put**](AsteriskApi.md#asterisk_logging_log_channel_name_rotate_put) | **PUT** /asterisk/logging/{logChannelName}/rotate | Rotates a log channel.
[**asterisk_modules_get**](AsteriskApi.md#asterisk_modules_get) | **GET** /asterisk/modules | List Asterisk modules.
[**asterisk_modules_module_name_delete**](AsteriskApi.md#asterisk_modules_module_name_delete) | **DELETE** /asterisk/modules/{moduleName} | Unload an Asterisk module.
[**asterisk_modules_module_name_get**](AsteriskApi.md#asterisk_modules_module_name_get) | **GET** /asterisk/modules/{moduleName} | Get Asterisk module information.
[**asterisk_modules_module_name_post**](AsteriskApi.md#asterisk_modules_module_name_post) | **POST** /asterisk/modules/{moduleName} | Load an Asterisk module.
[**asterisk_modules_module_name_put**](AsteriskApi.md#asterisk_modules_module_name_put) | **PUT** /asterisk/modules/{moduleName} | Reload an Asterisk module.
[**asterisk_ping_get**](AsteriskApi.md#asterisk_ping_get) | **GET** /asterisk/ping | Response pong message.
[**asterisk_variable_get**](AsteriskApi.md#asterisk_variable_get) | **GET** /asterisk/variable | Get the value of a global variable.
[**asterisk_variable_post**](AsteriskApi.md#asterisk_variable_post) | **POST** /asterisk/variable | Set the value of a global variable.


# **asterisk_config_dynamic_config_class_object_type_id_delete**
> asterisk_config_dynamic_config_class_object_type_id_delete(config_class, object_type, id)

Delete a dynamic configuration object.

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
api_instance = swagger_client.AsteriskApi(swagger_client.ApiClient(configuration))
config_class = 'config_class_example' # str | The configuration class containing dynamic configuration objects.
object_type = 'object_type_example' # str | The type of configuration object to delete.
id = 'id_example' # str | The unique identifier of the object to delete.

try:
    # Delete a dynamic configuration object.
    api_instance.asterisk_config_dynamic_config_class_object_type_id_delete(config_class, object_type, id)
except ApiException as e:
    print("Exception when calling AsteriskApi->asterisk_config_dynamic_config_class_object_type_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_class** | **str**| The configuration class containing dynamic configuration objects. | 
 **object_type** | **str**| The type of configuration object to delete. | 
 **id** | **str**| The unique identifier of the object to delete. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asterisk_config_dynamic_config_class_object_type_id_get**
> list[ConfigTuple] asterisk_config_dynamic_config_class_object_type_id_get(config_class, object_type, id)

Retrieve a dynamic configuration object.

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
api_instance = swagger_client.AsteriskApi(swagger_client.ApiClient(configuration))
config_class = 'config_class_example' # str | The configuration class containing dynamic configuration objects.
object_type = 'object_type_example' # str | The type of configuration object to retrieve.
id = 'id_example' # str | The unique identifier of the object to retrieve.

try:
    # Retrieve a dynamic configuration object.
    api_response = api_instance.asterisk_config_dynamic_config_class_object_type_id_get(config_class, object_type, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AsteriskApi->asterisk_config_dynamic_config_class_object_type_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_class** | **str**| The configuration class containing dynamic configuration objects. | 
 **object_type** | **str**| The type of configuration object to retrieve. | 
 **id** | **str**| The unique identifier of the object to retrieve. | 

### Return type

[**list[ConfigTuple]**](ConfigTuple.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asterisk_config_dynamic_config_class_object_type_id_put**
> list[ConfigTuple] asterisk_config_dynamic_config_class_object_type_id_put(config_class, object_type, id, fields=fields)

Create or update a dynamic configuration object.

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
api_instance = swagger_client.AsteriskApi(swagger_client.ApiClient(configuration))
config_class = 'config_class_example' # str | The configuration class containing dynamic configuration objects.
object_type = 'object_type_example' # str | The type of configuration object to create or update.
id = 'id_example' # str | The unique identifier of the object to create or update.
fields = [swagger_client.ConfigTuple()] # list[ConfigTuple] | The body object should have a value that is a list of ConfigTuples, which provide the fields to update. Ex. [ { \"attribute\": \"directmedia\", \"value\": \"false\" } ] (optional)

try:
    # Create or update a dynamic configuration object.
    api_response = api_instance.asterisk_config_dynamic_config_class_object_type_id_put(config_class, object_type, id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AsteriskApi->asterisk_config_dynamic_config_class_object_type_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_class** | **str**| The configuration class containing dynamic configuration objects. | 
 **object_type** | **str**| The type of configuration object to create or update. | 
 **id** | **str**| The unique identifier of the object to create or update. | 
 **fields** | [**list[ConfigTuple]**](ConfigTuple.md)| The body object should have a value that is a list of ConfigTuples, which provide the fields to update. Ex. [ { \&quot;attribute\&quot;: \&quot;directmedia\&quot;, \&quot;value\&quot;: \&quot;false\&quot; } ] | [optional] 

### Return type

[**list[ConfigTuple]**](ConfigTuple.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asterisk_info_get**
> AsteriskInfo asterisk_info_get(only=only)

Gets Asterisk system information.

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
api_instance = swagger_client.AsteriskApi(swagger_client.ApiClient(configuration))
only = ['only_example'] # list[str] | Filter information returned (optional)

try:
    # Gets Asterisk system information.
    api_response = api_instance.asterisk_info_get(only=only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AsteriskApi->asterisk_info_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **only** | [**list[str]**](str.md)| Filter information returned | [optional] 

### Return type

[**AsteriskInfo**](AsteriskInfo.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asterisk_logging_get**
> list[LogChannel] asterisk_logging_get()

Gets Asterisk log channel information.

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
api_instance = swagger_client.AsteriskApi(swagger_client.ApiClient(configuration))

try:
    # Gets Asterisk log channel information.
    api_response = api_instance.asterisk_logging_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AsteriskApi->asterisk_logging_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[LogChannel]**](LogChannel.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asterisk_logging_log_channel_name_delete**
> asterisk_logging_log_channel_name_delete(log_channel_name)

Deletes a log channel.

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
api_instance = swagger_client.AsteriskApi(swagger_client.ApiClient(configuration))
log_channel_name = 'log_channel_name_example' # str | Log channels name

try:
    # Deletes a log channel.
    api_instance.asterisk_logging_log_channel_name_delete(log_channel_name)
except ApiException as e:
    print("Exception when calling AsteriskApi->asterisk_logging_log_channel_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_channel_name** | **str**| Log channels name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asterisk_logging_log_channel_name_post**
> asterisk_logging_log_channel_name_post(log_channel_name, configuration)

Adds a log channel.

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
api_instance = swagger_client.AsteriskApi(swagger_client.ApiClient(configuration))
log_channel_name = 'log_channel_name_example' # str | The log channel to add
configuration = 'configuration_example' # str | levels of the log channel

try:
    # Adds a log channel.
    api_instance.asterisk_logging_log_channel_name_post(log_channel_name, configuration)
except ApiException as e:
    print("Exception when calling AsteriskApi->asterisk_logging_log_channel_name_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_channel_name** | **str**| The log channel to add | 
 **configuration** | **str**| levels of the log channel | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asterisk_logging_log_channel_name_rotate_put**
> asterisk_logging_log_channel_name_rotate_put(log_channel_name)

Rotates a log channel.

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
api_instance = swagger_client.AsteriskApi(swagger_client.ApiClient(configuration))
log_channel_name = 'log_channel_name_example' # str | Log channel's name

try:
    # Rotates a log channel.
    api_instance.asterisk_logging_log_channel_name_rotate_put(log_channel_name)
except ApiException as e:
    print("Exception when calling AsteriskApi->asterisk_logging_log_channel_name_rotate_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **log_channel_name** | **str**| Log channel&#39;s name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asterisk_modules_get**
> list[Module] asterisk_modules_get()

List Asterisk modules.

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
api_instance = swagger_client.AsteriskApi(swagger_client.ApiClient(configuration))

try:
    # List Asterisk modules.
    api_response = api_instance.asterisk_modules_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AsteriskApi->asterisk_modules_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Module]**](Module.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asterisk_modules_module_name_delete**
> asterisk_modules_module_name_delete(module_name)

Unload an Asterisk module.

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
api_instance = swagger_client.AsteriskApi(swagger_client.ApiClient(configuration))
module_name = 'module_name_example' # str | Module's name

try:
    # Unload an Asterisk module.
    api_instance.asterisk_modules_module_name_delete(module_name)
except ApiException as e:
    print("Exception when calling AsteriskApi->asterisk_modules_module_name_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_name** | **str**| Module&#39;s name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asterisk_modules_module_name_get**
> Module asterisk_modules_module_name_get(module_name)

Get Asterisk module information.

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
api_instance = swagger_client.AsteriskApi(swagger_client.ApiClient(configuration))
module_name = 'module_name_example' # str | Module's name

try:
    # Get Asterisk module information.
    api_response = api_instance.asterisk_modules_module_name_get(module_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AsteriskApi->asterisk_modules_module_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_name** | **str**| Module&#39;s name | 

### Return type

[**Module**](Module.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asterisk_modules_module_name_post**
> asterisk_modules_module_name_post(module_name)

Load an Asterisk module.

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
api_instance = swagger_client.AsteriskApi(swagger_client.ApiClient(configuration))
module_name = 'module_name_example' # str | Module's name

try:
    # Load an Asterisk module.
    api_instance.asterisk_modules_module_name_post(module_name)
except ApiException as e:
    print("Exception when calling AsteriskApi->asterisk_modules_module_name_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_name** | **str**| Module&#39;s name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asterisk_modules_module_name_put**
> asterisk_modules_module_name_put(module_name)

Reload an Asterisk module.

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
api_instance = swagger_client.AsteriskApi(swagger_client.ApiClient(configuration))
module_name = 'module_name_example' # str | Module's name

try:
    # Reload an Asterisk module.
    api_instance.asterisk_modules_module_name_put(module_name)
except ApiException as e:
    print("Exception when calling AsteriskApi->asterisk_modules_module_name_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **module_name** | **str**| Module&#39;s name | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asterisk_ping_get**
> AsteriskPing asterisk_ping_get()

Response pong message.

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
api_instance = swagger_client.AsteriskApi(swagger_client.ApiClient(configuration))

try:
    # Response pong message.
    api_response = api_instance.asterisk_ping_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AsteriskApi->asterisk_ping_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AsteriskPing**](AsteriskPing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asterisk_variable_get**
> Variable asterisk_variable_get(variable)

Get the value of a global variable.

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
api_instance = swagger_client.AsteriskApi(swagger_client.ApiClient(configuration))
variable = 'variable_example' # str | The variable to get

try:
    # Get the value of a global variable.
    api_response = api_instance.asterisk_variable_get(variable)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AsteriskApi->asterisk_variable_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable** | **str**| The variable to get | 

### Return type

[**Variable**](Variable.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asterisk_variable_post**
> asterisk_variable_post(variable, value=value)

Set the value of a global variable.

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
api_instance = swagger_client.AsteriskApi(swagger_client.ApiClient(configuration))
variable = 'variable_example' # str | The variable to set
value = 'value_example' # str | The value to set the variable to (optional)

try:
    # Set the value of a global variable.
    api_instance.asterisk_variable_post(variable, value=value)
except ApiException as e:
    print("Exception when calling AsteriskApi->asterisk_variable_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variable** | **str**| The variable to set | 
 **value** | **str**| The value to set the variable to | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

