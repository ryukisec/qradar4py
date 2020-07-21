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
    def __init__(self, host, api_token, version='13.1', verify=True):
        if not isinstance(host, str) or not isinstance(api_token, str):
            raise TypeError('The host and the API token must be supplied as strings!')
        self.__baseurl = urljoin(host, 'api/')
        self.__header = {'Version': version,
                         'Accept': 'application/json',
                         'SEC': api_token}
        self.__verify = verify
        # Disable warnings if verify is set to False
        if not self.__verify:
            from requests.packages.urllib3.exceptions import InsecureRequestWarning
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

        self.analytics = Analytics(self.__baseurl, self.__header, self.__verify)
        self.application = Application(self.__baseurl, self.__header, self.__verify)
        self.ariel = Ariel(self.__baseurl, self.__header, self.__verify)
        self.assetmodel = AssetModel(self.__baseurl, self.__header, self.__verify)
        self.auth = Auth(self.__baseurl, self.__header, self.__verify)
        self.backup_and_restore = BackupAndRestore(self.__baseurl, self.__header, self.__verify)
        self.bandwidth_manager = BandwidthManager(self.__baseurl, self.__header, self.__verify)
        self.config = Config(self.__baseurl, self.__header, self.__verify)
        self.configservices = Configservices(self.__baseurl, self.__header, self.__verify)
        self.configuration = Configuration(self.__baseurl, self.__header, self.__verify)
        self.dashboards = Dashboards(self.__baseurl, self.__header, self.__verify)
        self.dataclassification = DataClassification(self.__baseurl, self.__header, self.__verify)
        self.disaster_recovery = DisasterRecovery(self.__baseurl, self.__header, self.__verify)
        self.dynamic_search = DynamicSearch(self.__baseurl, self.__header, self.__verify)
        self.forensics = Forensics(self.__baseurl, self.__header, self.__verify)
        self.g11n = G11n(self.__baseurl, self.__header, self.__verify)
        self.guiappframework = GuiAppFramework(self.__baseurl, self.__header, self.__verify)
        self.health = Health(self.__baseurl, self.__header, self.__verify)
        self.healthdata = HealthData(self.__baseurl, self.__header, self.__verify)
        self.help = Help(self.__baseurl, self.__header, self.__verify)
        self.historicalcorrelation = HistoricalCorrelation(self.__baseurl, self.__header, self.__verify)
        self.internal = Internal(self.__baseurl, self.__header, self.__verify)
        self.qni = Qni(self.__baseurl, self.__header, self.__verify)
        self.qvm = Qvm(self.__baseurl, self.__header, self.__verify)
        self.referencedata = ReferenceData(self.__baseurl, self.__header, self.__verify)
        self.reporting = Reporting(self.__baseurl, self.__header, self.__verify)
        self.reports = Reports(self.__baseurl, self.__header, self.__verify)
        self.scanner = Scanner(self.__baseurl, self.__header, self.__verify)
        self.services = Services(self.__baseurl, self.__header, self.__verify)
        self.siem = Siem(self.__baseurl, self.__header, self.__verify)
        self.stagedconfig = StagedConfig(self.__baseurl, self.__header, self.__verify)
        self.support = Support(self.__baseurl, self.__header, self.__verify)
        self.usermanagement = Usermanagement(self.__baseurl, self.__header, self.__verify)
