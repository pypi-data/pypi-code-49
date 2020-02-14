"""
# CDK-SPA-Deploy

This is an AWS CDK Construct to make deploying a single page website (Angular/React/Vue) to AWS S3 behind SSL/Cloudfront as easy as 5 lines of code.

## Installation and Usage

### Typescript

npm install --save cdk-spa-deploy

![cdk-spa-deploy example](https://raw.githubusercontent.com/nideveloper/cdk-spa-deploy/master/img/spadeploy.png)

### Python

pip install cdk-spa-deploy

![cdk-spa-deploy python example](https://raw.githubusercontent.com/nideveloper/cdk-spa-deploy/master/img/python.png)

## Advanced Usage

### Auto Deploy From Hosted Zone Name

If you purchased your domain through route 53 and already have a hosted zone then just use the name to deploy your site behind cloudfront. This handles the SSL cert and everything for you.

![cdk-spa-deploy alias](https://raw.githubusercontent.com/nideveloper/cdk-spa-deploy/master/img/fromHostedZone.PNG)

### Custom Domain and SSL Certificates

You can also pass the ARN for an SSL certification and your alias routes to cloudfront

![cdk-spa-deploy alias](https://raw.githubusercontent.com/nideveloper/cdk-spa-deploy/master/img/cdkdeploy-alias.png)

### Encrypted S3 Bucket

Pass in one boolean to tell SPA Deploy to encrypt your website bucket

![cdk-spa-deploy encryption](https://raw.githubusercontent.com/nideveloper/cdk-spa-deploy/master/img/encryption.PNG)

### Restrict Access to Known IPs

Pass in a boolean and an array of IP addresses and your site is locked down!

![cdk-spa-deploy ipfilter](https://raw.githubusercontent.com/nideveloper/cdk-spa-deploy/master/img/ipfilter.png)

## Issues / Feature Requests

https://github.com/nideveloper/CDK-SPA-Deploy
"""
import abc
import builtins
import datetime
import enum
import typing

import jsii
import jsii.compat
import publication

import aws_cdk.aws_certificatemanager
import aws_cdk.aws_cloudfront
import aws_cdk.aws_route53_patterns
import aws_cdk.aws_route53_targets
import aws_cdk.aws_s3
import aws_cdk.aws_s3_deployment
import aws_cdk.core

__jsii_assembly__ = jsii.JSIIAssembly.load("cdk-spa-deploy", "0.6.0", __name__, "cdk-spa-deploy@0.6.0.jsii.tgz")


@jsii.data_type(jsii_type="cdk-spa-deploy.HostedZoneConfig", jsii_struct_bases=[], name_mapping={'index_doc': 'indexDoc', 'website_folder': 'websiteFolder', 'zone_name': 'zoneName'})
class HostedZoneConfig():
    def __init__(self, *, index_doc: str, website_folder: str, zone_name: str):
        """
        :param index_doc: -
        :param website_folder: -
        :param zone_name: -
        """
        self._values = {
            'index_doc': index_doc,
            'website_folder': website_folder,
            'zone_name': zone_name,
        }

    @builtins.property
    def index_doc(self) -> str:
        return self._values.get('index_doc')

    @builtins.property
    def website_folder(self) -> str:
        return self._values.get('website_folder')

    @builtins.property
    def zone_name(self) -> str:
        return self._values.get('zone_name')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'HostedZoneConfig(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


class SPADeploy(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="cdk-spa-deploy.SPADeploy"):
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, encrypt_bucket: typing.Optional[bool]=None, ip_filter: typing.Optional[bool]=None, ip_list: typing.Optional[typing.List[str]]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param encrypt_bucket: -
        :param ip_filter: -
        :param ip_list: -
        """
        config = SPAGlobalConfig(encrypt_bucket=encrypt_bucket, ip_filter=ip_filter, ip_list=ip_list)

        jsii.create(SPADeploy, self, [scope, id, config])

    @jsii.member(jsii_name="createBasicSite")
    def create_basic_site(self, *, index_doc: str, website_folder: str, certificate_arn: typing.Optional[str]=None, cf_aliases: typing.Optional[typing.List[str]]=None) -> None:
        """Basic setup needed for a non-ssl, non vanity url, non cached s3 website.

        :param index_doc: -
        :param website_folder: -
        :param certificate_arn: -
        :param cf_aliases: -
        """
        config = SPADeployConfig(index_doc=index_doc, website_folder=website_folder, certificate_arn=certificate_arn, cf_aliases=cf_aliases)

        return jsii.invoke(self, "createBasicSite", [config])

    @jsii.member(jsii_name="createSiteFromHostedZone")
    def create_site_from_hosted_zone(self, *, index_doc: str, website_folder: str, zone_name: str) -> None:
        """S3 Deployment, cloudfront distribution, ssl cert and error forwarding auto configured by using the details in the hosted zone provided.

        :param index_doc: -
        :param website_folder: -
        :param zone_name: -
        """
        config = HostedZoneConfig(index_doc=index_doc, website_folder=website_folder, zone_name=zone_name)

        return jsii.invoke(self, "createSiteFromHostedZone", [config])

    @jsii.member(jsii_name="createSiteWithCloudfront")
    def create_site_with_cloudfront(self, *, index_doc: str, website_folder: str, certificate_arn: typing.Optional[str]=None, cf_aliases: typing.Optional[typing.List[str]]=None) -> None:
        """This will create an s3 deployment fronted by a cloudfront distribution It will also setup error forwarding and unauth forwarding back to indexDoc.

        :param index_doc: -
        :param website_folder: -
        :param certificate_arn: -
        :param cf_aliases: -
        """
        config = SPADeployConfig(index_doc=index_doc, website_folder=website_folder, certificate_arn=certificate_arn, cf_aliases=cf_aliases)

        return jsii.invoke(self, "createSiteWithCloudfront", [config])

    @builtins.property
    @jsii.member(jsii_name="globalConfig")
    def global_config(self) -> "SPAGlobalConfig":
        return jsii.get(self, "globalConfig")

    @global_config.setter
    def global_config(self, value: "SPAGlobalConfig"):
        jsii.set(self, "globalConfig", value)


@jsii.data_type(jsii_type="cdk-spa-deploy.SPADeployConfig", jsii_struct_bases=[], name_mapping={'index_doc': 'indexDoc', 'website_folder': 'websiteFolder', 'certificate_arn': 'certificateARN', 'cf_aliases': 'cfAliases'})
class SPADeployConfig():
    def __init__(self, *, index_doc: str, website_folder: str, certificate_arn: typing.Optional[str]=None, cf_aliases: typing.Optional[typing.List[str]]=None):
        """
        :param index_doc: -
        :param website_folder: -
        :param certificate_arn: -
        :param cf_aliases: -
        """
        self._values = {
            'index_doc': index_doc,
            'website_folder': website_folder,
        }
        if certificate_arn is not None: self._values["certificate_arn"] = certificate_arn
        if cf_aliases is not None: self._values["cf_aliases"] = cf_aliases

    @builtins.property
    def index_doc(self) -> str:
        return self._values.get('index_doc')

    @builtins.property
    def website_folder(self) -> str:
        return self._values.get('website_folder')

    @builtins.property
    def certificate_arn(self) -> typing.Optional[str]:
        return self._values.get('certificate_arn')

    @builtins.property
    def cf_aliases(self) -> typing.Optional[typing.List[str]]:
        return self._values.get('cf_aliases')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SPADeployConfig(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


@jsii.data_type(jsii_type="cdk-spa-deploy.SPAGlobalConfig", jsii_struct_bases=[], name_mapping={'encrypt_bucket': 'encryptBucket', 'ip_filter': 'ipFilter', 'ip_list': 'ipList'})
class SPAGlobalConfig():
    def __init__(self, *, encrypt_bucket: typing.Optional[bool]=None, ip_filter: typing.Optional[bool]=None, ip_list: typing.Optional[typing.List[str]]=None):
        """
        :param encrypt_bucket: -
        :param ip_filter: -
        :param ip_list: -
        """
        self._values = {
        }
        if encrypt_bucket is not None: self._values["encrypt_bucket"] = encrypt_bucket
        if ip_filter is not None: self._values["ip_filter"] = ip_filter
        if ip_list is not None: self._values["ip_list"] = ip_list

    @builtins.property
    def encrypt_bucket(self) -> typing.Optional[bool]:
        return self._values.get('encrypt_bucket')

    @builtins.property
    def ip_filter(self) -> typing.Optional[bool]:
        return self._values.get('ip_filter')

    @builtins.property
    def ip_list(self) -> typing.Optional[typing.List[str]]:
        return self._values.get('ip_list')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'SPAGlobalConfig(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["HostedZoneConfig", "SPADeploy", "SPADeployConfig", "SPAGlobalConfig", "__jsii_assembly__"]

publication.publish()
