# coding=utf-8
# Licensed Materials - Property of IBM
# Copyright IBM Corp. 2019

import os
from tempfile import mkstemp
import streamsx.spl.op
import streamsx.spl.toolkit as toolkit
import streamsx.spl.types
from streamsx.topology.schema import CommonSchema, StreamSchema
from streamsx.spl.types import rstring
import datetime
from streamsx.toolkits import download_toolkit

_TOOLKIT_NAME = 'com.ibm.streamsx.jms'



#ProducerInputSchema = StreamSchema('tuple<>')
#"""Input schema for the data that is put onto the JMS broker.
#"""

#ProducerErrorOutputSchema = StreamSchema('tuple<tuple<> inputTuple, rstring errMsg>')
#"""Output schema for optional error output port.
#"""

#ConsumerOutputSchema = StreamSchema('tuple<>')
#"""Output schema for the data that is received from the JMS broker.
#"""

ConsumerErrorOutputSchema = StreamSchema('tuple<rstring errorMessage>')
"""Output schema for optional error output port.
"""



def _add_connection_document_file(topology, connection_document):
    if os.path.isfile(connection_document):
        return topology.add_file_dependency(connection_document, 'etc')
    else:
        raise ValueError("Parameter connection document='" + str(connection_document) + "' does not point to an existing file.")



def _add_java_class_libs(topology, java_class_libs):
    location_root = "opt"
    lib_paths_in_bundle = []

    for libs_item in java_class_libs:
        if os.path.isfile(libs_item):
            location = location_root #+ os.path.dirname(libs_item)
            lib_paths_in_bundle.append(topology.add_file_dependency(libs_item, location))

        elif os.path.isdir(libs_item):
            location = location_root #+ libs_item
            file_added = False

            for dir_entry in os.listdir(libs_item):
                file_path = os.path.join(libs_item, dir_entry)
                if os.path.isfile(file_path):
                    topology.add_file_dependency(file_path, location)
                    file_added = True

            if file_added:
                lib_paths_in_bundle.append(location)

        else:
            raise ValueError("The value '" + str(lib_item) + "' passed to parameter 'java_class_libs' does not point to an existing file or directory.")

    return lib_paths_in_bundle



def download_toolkit(url=None, target_dir=None):
    r"""Downloads the latest JMS toolkit from GitHub.

    Example for updating the JMS toolkit for your topology with the latest toolkit from GitHub::

        import streamsx.jms as jms
        # download JMS toolkit from GitHub
        jms_toolkit_location = jms.download_toolkit()
        # add the toolkit to topology
        streamsx.spl.toolkit.add_toolkit(topology, jms_toolkit_location)

    Example for updating the topology with a specific version of the JMS toolkit using a URL::

        import streamsx.jms as jms
        url122 = 'https://github.com/IBMStreams/streamsx.jms/releases/download/v1.2.2/streamsx.jms.toolkits-1.2.2-20190826-1516.tgz'
        jms_toolkit_location = jms.download_toolkit(url=url122)
        streamsx.spl.toolkit.add_toolkit(topology, jms_toolkit_location)

    Args:
        url(str): Link to toolkit archive (\*.tgz) to be downloaded. Use this parameter to download a specific version of the toolkit.
        target_dir(str): the directory where the toolkit is unpacked to. If a relative path is given,
            the path is appended to the system temporary directory, for example to /tmp on Unix/Linux systems.
            If target_dir is ``None`` a location relative to the system temporary directory is chosen.

    Returns:
        str: the location of the downloaded JMS toolkit

    .. note:: This function requires an outgoing Internet connection
    .. versionadded:: 0.1
    """
    _toolkit_location = streamsx.toolkits.download_toolkit (toolkit_name=_TOOLKIT_NAME, url=url, target_dir=target_dir)
    return _toolkit_location



def consume(topology, schemas, java_class_libs, connection, access, connection_document=None,
            app_configuration_name=None, user_property_name=None, password_property_name=None,
            ssl_connection=None, ssl_debug=None, key_store=None, key_store_password=None, trust_store=None, trust_store_password=None,
            jms_destination_outattribute_name=None, jms_deliverymode_outattribute_name=None, jms_expiration_outattribute_name=None, jms_priority_outattribute_name=None,
            jms_messageid_outattribute_name=None, jms_timestamp_outattribute_name=None, jms_correlationid_outattribute_name=None, jms_replyto_outattribute_name=None,
            jms_type_outattribute_name=None, jms_redelivered_outattribute_name=None, jms_header_properties=None, jms_header_properties_outattribute_name=None,
            message_selector=None, trigger_count=None, codepage=None, reconnection_policy=None, reconnection_bound=None, period=None, name=None):
    """Consume messages provided by a JMS broker.

    Args:
        topology(Topology): The Streams topology.
        schemas(): The schemas of the output ports. There is the mandatory data output port containing the data of the received messages and an optional error output port. The latter expecting something like the ConsumerErrorOutputSchema.

        java_class_libs(list str): Paths to JAR files containing the necessary classes to communicate with the JMS server. A single list entry may point to a JAR file or a directory.

        connection(str): This mandatory parameter identifies the name of the connection specification that contains an JMS element.
        access(str): This mandatory parameter identifies the access specification name.
        connection_document(str): Specifies the path name to the file that contains the connection and access specifications, which are identified by the **connection** and **access** parameters. If this parameter is not specified, the operator uses the file that is in the default location `./etc/connections.xml`.

        app_configuration_name(str): Specifies the name of application configuration that stores client credential information, the credential specified via application configuration overrides the one specified in connections file.
        user_property_name(str): Specifies the property name of user name in the application configuration. If the appConfigName parameter is specified and the userPropName parameter is not set, a compile time error occurs.
        password_property_name(str): Specifies the property name of the password in the application configuration. If the appConfigName parameter is specified and the passwordPropName parameter is not set, a compile time error occurs.

        ssl_connection(bool): Specifies whether the operator should attempt to connect using SSL. If this parameter is specified, then the *keyStore* and *trustStore* parameters must also be specified.
        ssl_debug(bool): Enable SSL/TLS protocol debugging. If enabled all protocol data and information is logged to the console.
        key_store(str): Specifies the path to the keyStore. If a relative path is specified, the path is relative to the application directory.
        key_store_password(str): Specifies the password for the keyStore.
        trust_store(str): Specifies the path to the trustStore. If a relative path is specified, the path is relative to the application directory.
        trust_store_password(str): Specifies the password for the trustStore.


        jms_destination_outattribute_name(str): Output attribute on output data stream to assign JMSDestination to, the specified attribute in output stream must be of type rstring.
        jms_deliverymode_outattribute_name(str): Output attribute on output data stream to assign JMSDeliveryMode to, the specified attribute in output stream must be of type int32.
        jms_expiration_outattribute_name(str): Output attribute on output data stream to assign JMSExpiration to, the specified attribute in output stream must be of type int64.
        jms_priority_outattribute_name(str): Output attribute on output data stream to assign JMSPriority to, the specified attribute in output stream must be of type int32.
        jms_messageid_outattribute_name(str): Output attribute on output data stream to assign JMSMessageID to, the specified attribute in output stream must be of type rstring.
        jms_timestamp_outattribute_name(str): Output attribute on output data stream to assign JMSTimestamp to, the specified attribute in output stream must be of type int64.
        jms_correlationid_outattribute_name(str): Output attribute on output data stream to assign JMSCorrelationID to, the specified attribute in output stream must be of type rstring.
        jms_replyto_outattribute_name(str): Output attribute on output data stream to assign JMSReplyTo to, the specified attribute in output stream must be of type rstring.
        jms_type_outattribute_name(str): Output attribute on output data stream to assign JMSType to, the specified attribute in output stream must be of type rstring.
        jms_redelivered_outattribute_name(str): Output attribute on output data stream to assign JMSRedelivered to, the specified attribute in output stream must be of type boolean.
        jms_header_properties(str): Specifies the mapping between JMS Header property values and Streams tuple attributes. The format of the mapping is: propertyName1/streamsAttributeName1/typeSpecifier1, propertyName2/streamsAttributeName2/typeSpecifier2,...
        jms_header_properties_outattribute_name(str): Output attribute on output data stream to assign to the map containing all received properties. The specified attribute in output stream must be of type map<ustring,ustring>.

        message_selector(str): This optional parameter is used as JMS Message Selector.
        trigger_count(int): Specifies how many messages are submitted before the JMSSource operator starts to drain the pipeline and establish a consistent state. This parameter must be greater than zero and must be set if the JMSSource operator is the start operator of an operatorDriven consistent region.
        codepage(str): Specifies the code page of the target system that is used to convert ustring for a Bytes message type.
        reconnection_policy(str): Specifies the reconnection policy. Valid values are `NoRetry`, `InfiniteRetry`, and `BoundedRetry`. If the parameter is not specified, the reconnection policy is set to `BoundedRetry` with a **reconnectionBound** of `5` and a **period** of 60 seconds.
        reconnection_bound(int): Specifies the number of successive connections that are attempted for an operator. You can use this parameter only when the **reconnectionPolicy** parameter is specified and set to `BoundedRetry`, otherwise a run time error occurs. If the **reconnectionBound** parameter is specified and the **reconnectionPolicy** parameter is not set, a compile time error occurs. The default value for the **reconnectionBound** parameter is `5`.
        period(double): Specifies the time period in seconds the operator waits before it tries to reconnect. You can use this parameter only when the **reconnectionPolicy** parameter is specified, otherwise a compile time error occurs. The default value for the **period** parameter is `60`.

        name(str): Source name in the Streams context, defaults to a generated name.

    Returns:
        Output Stream containing the data of the received messages.
        Optional Error Output Stream with schema :py:const:`~streamsx.jms.ConsumerErrorOutputSchema`.
    """

    if(java_class_libs is None):
        raise ValueError("You have to provide the paths to the Java class libraries.")

    # Plausibility check of SSL parameters
    if (ssl_connection is not None and (key_store is None or key_store_password is None or trust_store is None or trust_store_password is None)):
        raise ValueError("If ssl_connection is enabled, parameters 'key_store', 'key_store_password', 'trust_store', and 'trust_store_password' must be set, too.")

    _op = _JMSSource(topology, schemas=schemas, classLibs=java_class_libs, connection=connection, access=access, connectionDocument=connection_document,
                    appConfigName=app_configuration_name, userPropName=user_property_name, passwordPropName=password_property_name,
                    sslConnection=ssl_connection, sslDebug=ssl_debug, keyStore=key_store, keyStorePassword=key_store_password, trustStore=trust_store, trustStorePassword=trust_store_password,
                    jmsDestinationOutAttributeName=jms_destination_outattribute_name, jmsDeliveryModeOutAttributeName=jms_deliverymode_outattribute_name,
                    jmsExpirationOutAttributeName=jms_expiration_outattribute_name, jmsPriorityOutAttributeName=jms_priority_outattribute_name,
                    jmsMessageIDOutAttributeName=jms_messageid_outattribute_name, jmsTimestampOutAttributeName=jms_timestamp_outattribute_name,
                    jmsCorrelationIDOutAttributeName=jms_correlationid_outattribute_name, jmsReplyToOutAttributeName=jms_replyto_outattribute_name,
                    jmsTypeOutAttributeName=jms_type_outattribute_name, jmsRedeliveredOutAttributeName=jms_redelivered_outattribute_name,
                    jmsHeaderProperties=jms_header_properties, jmsHeaderPropertiesOutAttributeName=jms_header_properties_outattribute_name,
                    messageSelector=message_selector, triggerCount=trigger_count, codepage=codepage, reconnectionPolicy=reconnection_policy,
                    reconnectionBound=reconnection_bound, period=period, name=name)

    if(java_class_libs is not None):
        bundled_class_lib_paths = _add_java_class_libs(topology, java_class_libs)
        i = 0
        class_libs_path_strings = ''
        for path in bundled_class_lib_paths:
            if i > 0:
                class_libs_path_strings += ", "
            i += 1
            class_libs_path_strings += "'" + path + "'"
        _op.params['classLibs'] = _op.expression(class_libs_path_strings)


    if connection_document is not None:
        _op.params['connectionDocument'] = _op.expression("getThisToolkitDir() + '/" + _add_connection_document_file(topology, connection_document) + "'")

    return _op.outputs



def produce(stream, schema, java_class_libs, connection, access, connection_document=None,
            app_configuration_name=None, user_property_name=None, password_property_name=None,
            ssl_connection=None, ssl_debug=None, key_store=None, key_store_password=None, trust_store=None, trust_store_password=None,
            jms_header_properties=None, codepage=None, reconnection_policy=None, reconnection_bound=None, period=None,
            consistent_region_queue_name=None, max_message_send_retries=None, message_send_retry_delay=None, name=None):
    """Send messages to a JMS broker.

    Args:
        stream: The input stream containing the data to send to the JMS broker
        schema: The schema of the optional error output port.

        java_class_libs(list str): Paths to JAR files containing the necessary classes to communicate with the JMS server. A single list entry may point to a JAR file or a directory.

        connection(str): This mandatory parameter identifies the name of the connection specification that contains an JMS element.
        access(str): This mandatory parameter identifies the access specification name.
        connection_document(str): Specifies the path name to the file that contains the connection and access specifications, which are identified by the **connection** and **access** parameters. If this parameter is not specified, the operator uses the file that is in the default location `./etc/connections.xml`.

        app_configuration_name(str): Specifies the name of application configuration that stores client credential information, the credential specified via application configuration overrides the one specified in connections file.
        user_property_name(str): Specifies the property name of user name in the application configuration. If the appConfigName parameter is specified and the userPropName parameter is not set, a compile time error occurs.
        password_property_name(str): Specifies the property name of the password in the application configuration. If the appConfigName parameter is specified and the passwordPropName parameter is not set, a compile time error occurs.

        ssl_connection(bool): Specifies whether the operator should attempt to connect using SSL. If this parameter is specified, then the *keyStore* and *trustStore* parameters must also be specified.
        ssl_debug(bool): Enable SSL/TLS protocol debugging. If enabled all protocol data and information is logged to the console.
        key_store(str): Specifies the path to the keyStore. If a relative path is specified, the path is relative to the application directory.
        key_store_password(str): Specifies the password for the keyStore.
        trust_store(str): Specifies the path to the trustStore. If a relative path is specified, the path is relative to the application directory.
        trust_store_password(str): Specifies the password for the trustStore.

        jms_header_properties(str): Specifies the mapping between JMS Header property values and Streams tuple attributes. The format of the mapping is: propertyName1/streamsAttributeName1/typeSpecifier1, propertyName2/streamsAttributeName2/typeSpecifier2,...

        codepage(str): Specifies the code page of the target system that is used to convert ustring for a Bytes message type.
        reconnection_policy(str): Specifies the reconnection policy. Valid values are `NoRetry`, `InfiniteRetry`, and `BoundedRetry`. If the parameter is not specified, the reconnection policy is set to `BoundedRetry` with a **reconnectionBound** of `5` and a **period** of 60 seconds.
        reconnection_bound(int): Specifies the number of successive connections that are attempted for an operator. You can use this parameter only when the **reconnectionPolicy** parameter is specified and set to `BoundedRetry`, otherwise a run time error occurs. If the **reconnectionBound** parameter is specified and the **reconnectionPolicy** parameter is not set, a compile time error occurs. The default value for the **reconnectionBound** parameter is `5`.
        period(double): Specifies the time period in seconds the operator waits before it tries to reconnect. You can use this parameter only when the **reconnectionPolicy** parameter is specified, otherwise a compile time error occurs. The default value for the **period** parameter is `60`.

        consistent_region_queue_name(str): This is a required parameter if this operator is participating in a consistent region. This parameter specifies the queue to be used to store consistent region specific information and the operator will perform a JNDI lookup with the queue name specified at initialization state. The queue name specified must also exist on the same messaging server where this operator is establishing the connection.

        max_message_send_retries(int): Specifies the number of successive retries that are attempted for a message if a failure occurs when the message is sent. The default value is zero; no retries are attempted.
        message_send_retry_delay(long): Specifies the time in milliseconds to wait before the next delivery attempt. If the **maxMessageSendRetries** is specified, you must also specify a value for this parameter.

        name(str): Source name in the Streams context, defaults to a generated name.

    Returns:
        Optional error output Stream with schema ???
    """

    if(java_class_libs is None):
        raise ValueError("You have to provide the paths to the Java class libraries.")

    # Plausibility check of SSL parameters
    if (ssl_connection is not None and (key_store is None or key_store_password is None or trust_store is None or trust_store_password is None)):
        raise ValueError("If ssl_connection is enabled, parameters 'key_store', 'key_store_password', 'trust_store', and 'trust_store_password' must be set, too.")

    _op = _JMSSink(stream, schema, classLibs=java_class_libs, connection=connection, access=access, connectionDocument=connection_document,
                    appConfigName=app_configuration_name, userPropName=user_property_name, passwordPropName=password_property_name,
                    sslConnection=ssl_connection, sslDebug=ssl_debug, keyStore=key_store, keyStorePassword=key_store_password, trustStore=trust_store, trustStorePassword=trust_store_password,
                    jmsHeaderProperties=jms_header_properties, codepage=codepage, reconnectionPolicy=reconnection_policy, reconnectionBound=reconnection_bound, period=period,
                    consistentRegionQueueName=consistent_region_queue_name, maxMessageSendRetries=max_message_send_retries, messageSendRetryDelay=message_send_retry_delay, name=name)

    if(java_class_libs is not None):
        bundled_class_lib_paths = _add_java_class_libs(stream.topology, java_class_libs)
        i = 0
        class_libs_path_strings = ''
        for path in bundled_class_lib_paths:
            if i > 0:
                class_libs_path_strings += ", "
            i += 1
            class_libs_path_strings += "'" + path + "'"
        _op.params['classLibs'] = _op.expression(class_libs_path_strings)

    if connection_document is not None:
        _op.params['connectionDocument'] = _op.expression("getThisToolkitDir() + '/" + _add_connection_document_file(stream.topology, connection_document) + "'")

    if schema is not None:
        return _op.outputs[0]

#   return _op.outputs[0]



class _JMSSource(streamsx.spl.op.Invoke):
    def __init__(self, topology, schemas, classLibs=None, connection=None, access=None, connectionDocument=None,
                 appConfigName=None, userPropName=None, passwordPropName=None,
                 sslConnection=None, sslDebug=None, keyStore=None, keyStorePassword=None, trustStore=None, trustStorePassword=None,
                 jmsDestinationOutAttributeName=None, jmsDeliveryModeOutAttributeName=None, jmsExpirationOutAttributeName=None, jmsPriorityOutAttributeName=None,
                 jmsMessageIDOutAttributeName=None, jmsTimestampOutAttributeName=None, jmsCorrelationIDOutAttributeName=None, jmsReplyToOutAttributeName=None,
                 jmsTypeOutAttributeName=None, jmsRedeliveredOutAttributeName=None, jmsHeaderProperties=None, jmsHeaderPropertiesOutAttributeName=None,
                 messageSelector=None, triggerCount=None, codepage=None, reconnectionPolicy=None, reconnectionBound=None, period=None,
                 vmArg=None, name=None):

        toolkit.add_toolkit_dependency(topology, "com.ibm.streamsx.jms", "[2.0.0,10.0.0)")

        kind="com.ibm.streamsx.jms::JMSSource"


        params = dict()

        if classLibs is not None:
            params['classLibs'] = classLibs

        if connection is not None:
            params['connection'] = connection
        if connection is not None:
            params['access'] = access
        if connectionDocument is not None:
            params['connectionDocument'] = connectionDocument

        if appConfigName is not None:
            params['appConfigName'] = appConfigName
        if userPropName is not None:
            params['userPropName'] = userPropName
        if passwordPropName is not None:
            params['passwordPropName'] = passwordPropName

        if sslConnection is not None:
            params['sslConnection'] = sslConnection
        if sslDebug is not None:
            params['sslDebug'] = sslDebug
        if keyStore is not None:
            params['keyStore'] = keyStore
        if keyStorePassword is not None:
            params['keyStorePassword'] = keyStorePassword
        if trustStore is not None:
            params['trustStore'] = trustStore
        if trustStorePassword is not None:
            params['trustStorePassword'] = trustStorePassword

        if jmsDestinationOutAttributeName is not None:
            params['jmsDestinationOutAttributeName'] = jmsDestinationOutAttributeName
        if jmsDeliveryModeOutAttributeName is not None:
            params['jmsDeliveryModeOutAttributeName'] = jmsDeliveryModeOutAttributeName
        if jmsExpirationOutAttributeName is not None:
            params['jmsExpirationOutAttributeName'] = jmsExpirationOutAttributeName
        if jmsPriorityOutAttributeName is not None:
            params['jmsPriorityOutAttributeName'] = jmsPriorityOutAttributeName
        if jmsMessageIDOutAttributeName is not None:
            params['jmsMessageIDOutAttributeName'] = jmsMessageIDOutAttributeName
        if jmsTimestampOutAttributeName is not None:
            params['jmsTimestampOutAttributeName'] = jmsTimestampOutAttributeName
        if jmsCorrelationIDOutAttributeName is not None:
            params['jmsCorrelationIDOutAttributeName'] = jmsCorrelationIDOutAttributeName
        if jmsReplyToOutAttributeName is not None:
            params['jmsReplyToOutAttributeName'] = jmsReplyToOutAttributeName
        if jmsTypeOutAttributeName is not None:
            params['jmsTypeOutAttributeName'] = jmsTypeOutAttributeName
        if jmsRedeliveredOutAttributeName is not None:
            params['jmsRedeliveredOutAttributeName'] = jmsRedeliveredOutAttributeName
        if jmsHeaderProperties is not None:
            params['jmsHeaderProperties'] = jmsHeaderProperties
        if jmsHeaderPropertiesOutAttributeName is not None:
            params['jmsHeaderPropertiesOutAttributeName'] = jmsHeaderPropertiesOutAttributeName

        if messageSelector is not None:
            params['messageSelector'] = messageSelector
        if triggerCount is not None:
            params['triggerCount'] = triggerCount
        if codepage is not None:
            params['codepage'] = codepage
        if reconnectionPolicy is not None:
            params['reconnectionPolicy'] = reconnectionPolicy
        if reconnectionBound is not None:
            params['reconnectionBound'] = reconnectionBound
        if period is not None:
            params['period'] = period

        if vmArg is not None:
            params['vmArg'] = vmArg

        super(_JMSSource, self).__init__(topology=topology, kind=kind, inputs=None, schemas=schemas, params=params, name=name)



class _JMSSink(streamsx.spl.op.Invoke):
    def __init__(self, stream, schema=None, classLibs=None, connection=None, access=None, connectionDocument=None,
                 appConfigName=None, userPropName=None, passwordPropName=None,
                 sslConnection=None, sslDebug=None, keyStore=None, keyStorePassword=None, trustStore=None, trustStorePassword=None,
                 jmsHeaderProperties=None, codepage=None, reconnectionPolicy=None, reconnectionBound=None, period=None,
                 consistentRegionQueueName=None, maxMessageSendRetries=None, messageSendRetryDelay=None,
                 vmArg=None, name=None):

        topology = stream.topology
        kind="com.ibm.streamsx.jms::JMSSink"
        inputs=[stream]
        schemas=[schema]

        toolkit.add_toolkit_dependency(topology, "com.ibm.streamsx.jms", "[2.0.0,10.0.0)")

        params = dict()

        if classLibs is not None:
            params['classLibs'] = classLibs

        if connection is not None:
            params['connection'] = connection
        if connection is not None:
            params['access'] = access
        if connectionDocument is not None:
            params['connectionDocument'] = connectionDocument

        if appConfigName is not None:
            params['appConfigName'] = appConfigName
        if userPropName is not None:
            params['userPropName'] = userPropName
        if passwordPropName is not None:
            params['passwordPropName'] = passwordPropName

        if sslConnection is not None:
            params['sslConnection'] = sslConnection
        if sslDebug is not None:
            params['sslDebug'] = sslDebug
        if keyStore is not None:
            params['keyStore'] = keyStore
        if keyStorePassword is not None:
            params['keyStorePassword'] = keyStorePassword
        if trustStore is not None:
            params['trustStore'] = trustStore
        if trustStorePassword is not None:
            params['trustStorePassword'] = trustStorePassword

        if jmsHeaderProperties is not None:
            params['jmsHeaderProperties'] = jmsHeaderProperties

        if codepage is not None:
            params['codepage'] = codepage
        if reconnectionPolicy is not None:
            params['reconnectionPolicy'] = reconnectionPolicy
        if reconnectionBound is not None:
            params['reconnectionBound'] = reconnectionBound
        if period is not None:
            params['period'] = period

        if consistentRegionQueueName is not None:
            params['consistentRegionQueueName'] = consistentRegionQueueName

        if maxMessageSendRetries is not None:
            params['maxMessageSendRetries'] = maxMessageSendRetries
        if messageSendRetryDelay is not None:
            params['messageSendRetryDelay'] = messageSendRetryDelay

        if vmArg is not None:
            params['vmArg'] = vmArg

        super(_JMSSink, self).__init__(topology=topology, kind=kind, inputs=inputs, schemas=schemas, params=params, name=name)
