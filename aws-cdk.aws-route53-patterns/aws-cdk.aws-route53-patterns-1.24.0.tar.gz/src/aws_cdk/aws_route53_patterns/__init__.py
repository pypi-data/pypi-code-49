"""
# Route53 Patterns for the CDK Route53 Library

<!--BEGIN STABILITY BANNER-->---


![Stability: Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

> **This is a *developer preview* (public beta) module. Releases might lack important features and might have
> future breaking changes.**
>
> This API is still under active development and subject to non-backward
> compatible changes or removal in any future version. Use of the API is not recommended in production
> environments. Experimental APIs are not subject to the Semantic Versioning model.

---
<!--END STABILITY BANNER-->

This library contains commonly used patterns for Route53.

## HTTPS Redirect

This construct allows creating a simple domainA -> domainB redirect using CloudFront and S3. You can specify multiple domains to be redirected.

```python
# Example automatically generated without compilation. See https://github.com/aws/jsii/issues/826
HttpsRedirect(stack, "Redirect",
    record_names=["foo.example.com"],
    target_domain="bar.example.com",
    zone=HostedZone.from_hosted_zone_attributes(stack, "HostedZone",
        hosted_zone_id="ID",
        zone_name="example.com"
    )
)
```

See the documentation of `@aws-cdk/aws-route53-patterns` for more information.
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
import aws_cdk.aws_iam
import aws_cdk.aws_route53
import aws_cdk.aws_route53_targets
import aws_cdk.aws_s3
import aws_cdk.core
import aws_cdk.region_info

__jsii_assembly__ = jsii.JSIIAssembly.load("@aws-cdk/aws-route53-patterns", "1.24.0", __name__, "aws-route53-patterns@1.24.0.jsii.tgz")


class HttpsRedirect(aws_cdk.core.Construct, metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-route53-patterns.HttpsRedirect"):
    """
    stability
    :stability: experimental
    """
    def __init__(self, scope: aws_cdk.core.Construct, id: str, *, target_domain: str, zone: aws_cdk.aws_route53.IHostedZone, certificate: typing.Optional[aws_cdk.aws_certificatemanager.ICertificate]=None, record_names: typing.Optional[typing.List[str]]=None) -> None:
        """
        :param scope: -
        :param id: -
        :param target_domain: The redirect target domain.
        :param zone: HostedZone of the domain.
        :param certificate: The ACM certificate; Has to be in us-east-1 Default: - create a new certificate in us-east-1
        :param record_names: The domain names to create that will redirect to ``targetDomain``. Default: - the domain name of the zone

        stability
        :stability: experimental
        """
        props = HttpsRedirectProps(target_domain=target_domain, zone=zone, certificate=certificate, record_names=record_names)

        jsii.create(HttpsRedirect, self, [scope, id, props])


@jsii.data_type(jsii_type="@aws-cdk/aws-route53-patterns.HttpsRedirectProps", jsii_struct_bases=[], name_mapping={'target_domain': 'targetDomain', 'zone': 'zone', 'certificate': 'certificate', 'record_names': 'recordNames'})
class HttpsRedirectProps():
    def __init__(self, *, target_domain: str, zone: aws_cdk.aws_route53.IHostedZone, certificate: typing.Optional[aws_cdk.aws_certificatemanager.ICertificate]=None, record_names: typing.Optional[typing.List[str]]=None):
        """
        :param target_domain: The redirect target domain.
        :param zone: HostedZone of the domain.
        :param certificate: The ACM certificate; Has to be in us-east-1 Default: - create a new certificate in us-east-1
        :param record_names: The domain names to create that will redirect to ``targetDomain``. Default: - the domain name of the zone

        stability
        :stability: experimental
        """
        self._values = {
            'target_domain': target_domain,
            'zone': zone,
        }
        if certificate is not None: self._values["certificate"] = certificate
        if record_names is not None: self._values["record_names"] = record_names

    @builtins.property
    def target_domain(self) -> str:
        """The redirect target domain.

        stability
        :stability: experimental
        """
        return self._values.get('target_domain')

    @builtins.property
    def zone(self) -> aws_cdk.aws_route53.IHostedZone:
        """HostedZone of the domain.

        stability
        :stability: experimental
        """
        return self._values.get('zone')

    @builtins.property
    def certificate(self) -> typing.Optional[aws_cdk.aws_certificatemanager.ICertificate]:
        """The ACM certificate;

        Has to be in us-east-1

        default
        :default: - create a new certificate in us-east-1

        stability
        :stability: experimental
        """
        return self._values.get('certificate')

    @builtins.property
    def record_names(self) -> typing.Optional[typing.List[str]]:
        """The domain names to create that will redirect to ``targetDomain``.

        default
        :default: - the domain name of the zone

        stability
        :stability: experimental
        """
        return self._values.get('record_names')

    def __eq__(self, rhs) -> bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs) -> bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return 'HttpsRedirectProps(%s)' % ', '.join(k + '=' + repr(v) for k, v in self._values.items())


__all__ = ["HttpsRedirect", "HttpsRedirectProps", "__jsii_assembly__"]

publication.publish()
