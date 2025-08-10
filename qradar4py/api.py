#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from urllib.parse import urljoin

from qradar4py.endpoints import *


class QRadarApi:
    """
    QRadar API wrapped in Python3
    :param host         The url of the QRadar installation.
    :param api_token    The token needed to access the API
    :param version      The version of the API to use.
    :param verify       Verify SSL certificate.
    """
    def __init__(self, host, api_token, version='25.0', verify=True):
        if not isinstance(host, str) or not isinstance(api_token, str):
            raise TypeError('The host and the API token must be supplied as strings!')
        self.__baseurl = urljoin(host, 'api/')

        self.session = requests.Session()
        self.session.headers.update({'Version': version,
                                     'Accept': 'application/json',
                                     'SEC': api_token})
        self.session.verify = verify
        
        # Disable warnings if verify is set to False
        if not verify:
            from requests.packages.urllib3.exceptions import InsecureRequestWarning
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

        self.access = Access(self.__baseurl, self.session)
        self.analytics = Analytics(self.__baseurl, self.session)
        self.application = Application(self.__baseurl, self.session)
        self.ariel = Ariel(self.__baseurl, self.session)
        self.assetmodel = AssetModel(self.__baseurl, self.session)
        self.auth = Auth(self.__baseurl, self.session)
        self.backup_and_restore = BackupAndRestore(self.__baseurl, self.session)
        self.bandwidth_manager = BandwidthManager(self.__baseurl, self.session)
        self.config = Config(self.__baseurl, self.session)
        self.configservices = Configservices(self.__baseurl, self.session)
        self.configuration = Configuration(self.__baseurl, self.session)
        self.dashboards = Dashboards(self.__baseurl, self.session)
        self.dataclassification = DataClassification(self.__baseurl, self.session)
        self.disaster_recovery = DisasterRecovery(self.__baseurl, self.session)
        self.dynamic_search = DynamicSearch(self.__baseurl, self.session)
        self.forensics = Forensics(self.__baseurl, self.session)
        self.g11n = G11n(self.__baseurl, self.session)
        self.guiappframework = GuiAppFramework(self.__baseurl, self.session)
        self.health = Health(self.__baseurl, self.session)
        self.healthdata = HealthData(self.__baseurl, self.session)
        self.help = Help(self.__baseurl, self.session)
        self.historicalcorrelation = HistoricalCorrelation(self.__baseurl, self.session)
        self.internal = Internal(self.__baseurl, self.session)
        self.qni = Qni(self.__baseurl, self.session)
        self.qvm = Qvm(self.__baseurl, self.session)
        self.referencedata = ReferenceData(self.__baseurl, self.session)
        self.referencedatacollections = ReferenceDataCollections(self.__baseurl, self.session)
        self.reporting = Reporting(self.__baseurl, self.session)
        self.reports = Reports(self.__baseurl, self.session)
        self.scanner = Scanner(self.__baseurl, self.session)
        self.services = Services(self.__baseurl, self.session)
        self.siem = Siem(self.__baseurl, self.session)
        self.stagedconfig = StagedConfig(self.__baseurl, self.session)
        self.support = Support(self.__baseurl, self.session)
        self.usermanagement = Usermanagement(self.__baseurl, self.session)
