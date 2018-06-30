from setuptools import setup, find_packages

install_requires = [

]

dependencies = [
    'https://github.com/gisce/hookshub/archive/master.zip'
]

setup(
    name='nice-hooks',
    version='0.1.0',
    author='Ytturi',
    author_email='ytturi@protonmail.com',
    url='https://github.com/ytturi/Twitter_GithubNotice',
    description='A Hook to capture activity and send tweets',
    long_description=__doc__,
    license='GNUv3',
    packages=find_packages(),
    install_requires=install_requires,
    dependency_links=dependencies,
    entry_points={
        'hookshub.plugins': [
            'twtnot_gh_merge = twitter_githubnotice.hooks:GHMergeHook'
            'twtnot_gh_push = twitter_githubnotice.hooks:GHMPushHook'
            'twtnot_gl_merge = twitter_githubnotice.hooks:GLMergeHook'
            'twtnot_gl_push = twitter_githubnotice.hooks:GLPushHook'
        ],
    },
    include_package_data=True,
)