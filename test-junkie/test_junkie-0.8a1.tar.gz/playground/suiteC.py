import time
from random import randint

from test_junkie.decorators import Suite, test, beforeClass, beforeTest, afterTest, afterClass
from test_junkie.meta import meta, Meta
from tests.junkie_suites.TestListener import TestListener


class AuthApiSuite:

    @beforeClass()
    def before_class1(self):
        print("Before class, should not see this")

    @test(component="Auth", tags=["api", "auth", "basic_auth"])
    def authenticate_via_basic_auth_api(self):
        """# Title

        Steps:

        1. Somethingsdfsdf sdfsdfkjsf slkfjslkfj
        2. sldkfjslf lsdkfjslakfdjaslkf lsdkfj salkf
        3. lsdkfjslkaf lsa dflksajflsakfj flsadfj salfkjsalkfj

        Spec: [Spec Link](https://google.com)

        - [x] This task is done
        - [ ] This is still pending


        | Tables        | Are           | Cool  |
        | ------------- |:-------------:| -----:|
        | **col 3 is**  | right-aligned | $1600 |
        | col 2 is      | *centered*    |   $12 |
        | zebra stripes | ~~are neat~~  |    $1 |
        """
        pass

    @test(component="Auth", tags=["api", "auth", "two_factor"], owner="Victor")
    def authenticate_via_two_factor_api(self):
        pass

    @test(component="Auth", tags=["api", "auth", "sso"], owner="Victor")
    def authenticate_via_sso(self):
        pass

    @test(component="Auth", tags=["api", "auth", "sso"], owner="Victor")
    def sso_hit_negative_auth_limit(self):
        # time.sleep(randint(0, 4))
        pass

    @test(component="Auth", tags=["api", "auth", "basic_auth"], owner="Victor")
    def auth_hit_negative_auth_limit(self):
        # time.sleep(randint(0, 4))
        pass

    @test(component="Auth", tags=["api", "auth", "two_factor"], owner="Victor")
    def two_factor_hit_negative_auth_limit(self):
        # time.sleep(randint(0, 4))
        pass
