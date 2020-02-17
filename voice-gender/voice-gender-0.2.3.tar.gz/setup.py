from setuptools import setup


setup(
    name='voice-gender',
    version='0.2.3',
    packages=['voice_gender'],
    install_requires=["numpy==1.15.2",
                      "python-speech-features==0.5",
                      "scikit-learn==0.19.2",
                      "scipy==1.1.0"],
    include_package_data=True,
    url='https://github.com/JarbasAl/voice-gender',
    license='MIT',
    author='jarbasAI',
    author_email='jarbasai@mailfence.com',
    description='recognize gender'
)
