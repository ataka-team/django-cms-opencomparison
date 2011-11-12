from setuptools import setup, find_packages

version = "0.0.0"

long_description=""
try:
    long_description=file('README').read()
except Exception:
    pass

license=""
try:
    license=file('MIT_License.txt').read()
except Exception:
    pass

setup(
    name = 'django-cms-opencomparison',
    version = version,
    description = 'Django CMS Opencomparison Plugins',
    author = 'Pablo Saavedra',
    author_email = 'pablo.saavedra@treitos.com',
    url = 'http://github.com/psaavedra/django-cms-opencomparison',
    download_url= 'https://github.com/psaavedra/django-cms-opencomparison/zipball/master',
    packages = find_packages(),
    package_data={
        'cms_opencomparison': [
            'templates/*/*.html',
            'static/*/css/*.css',
            'static/*/images/*',
            'static/*/js/*.js',
        ],
    },

    zip_safe=False,
    install_requires=[
        "django-cms>=2.1",
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description=long_description,
    license=license,
    keywords = "opencomparison django cms plugins",
)
