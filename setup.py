from setuptools import find_packages
from setuptools import setup


setup(
    name='ll.policy',
    version='0.4',
    description="Turns Plone Site into LL site.",
    long_description=open("README.rst").read(),
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@abita.fi',
    url='https://github.com/taito/ll.policy',
    license='Non-free',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['ll'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Products.PFGExtendedMailAdapter',
        'Products.PFGSelectionStringField',
        'abita.development',
        'collective.folderlogo',
        'collective.microsite',
        'collective.pfg.payment',
        'collective.pfg.showrequest',
        'hexagonit.testing',
        'll.theme',
        'setuptools',
        'sll.basepolicy',
        'sll.locales'],
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
