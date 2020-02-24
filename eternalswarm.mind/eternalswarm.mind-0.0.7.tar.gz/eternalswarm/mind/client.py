from typing import Any, List

import grpc

from . import (bloodhound_pb2, bloodhound_pb2_grpc, callback_pb2,
               callback_pb2_grpc, exploitation_pb2, exploitation_pb2_grpc,
               information_pb2, information_pb2_grpc, metasploit_pb2,
               metasploit_pb2_grpc, models_pb2, relaying_pb2,
               relaying_pb2_grpc, scanner_pb2, scanner_pb2_grpc, wireguard_pb2,
               wireguard_pb2_grpc)


class Client():

    def __init__(self, ip: str, port: int, ssl: bool = False, ca: str = None, cert: str = None, key: str = None):
        self.ip = ip
        self.port = port
        self.ssl = ssl
        self.ca = ca
        self.cert = cert
        self.key = key
        self._channel = None
        self.uid = ''

    @property
    def channel(self):
        """
            Channel and stuff...
        """
        if not self._channel:
            if self.ssl:
                credentials = grpc.ssl_channel_credentials(
                    self.ca, self.key, self.cert
                )
                options = ()
                if self.uid:
                    options = (
                        ('grpc.ssl_target_name_override', self.uid,),
                    )
                self._channel = grpc.secure_channel(
                    f"{self.ip}:{self.port}",
                    credentials,
                    options=options
                )
            else:
                self._channel = grpc.insecure_channel(
                    f"{self.ip}:{self.port}"
                )
        return self._channel

    def _perform_request(self, function, call_arguments):
        """
            Perform the request, this function will raise Exceptions and return the result otherwise.
        """
        try:
            result = function(call_arguments)
            return result
        except grpc._channel._Rendezvous as e:
            if e.code() == grpc.StatusCode.UNAVAILABLE:
                self._channel = None
            raise e
        except Exception as e:
            self._channel = None
            raise e

    def perform_request(self, function, call_arguments):
        """
            Perform the request
        """
        return self._perform_request(function, call_arguments)


    @staticmethod
    def create_pagination_message(scan_id: int, **kwargs) -> models_pb2.Pagination:
        """
            Create a pagination message from the given arguments.
        """
        scan = models_pb2.Scan(id=scan_id)
        pagination = models_pb2.Pagination(scan=scan)
        for key, value in kwargs.items():
            try:
                setattr(pagination, key, value)
            except AttributeError:
                pass
        return pagination


class DroneClient(Client):
    """
        Client class to talk with drones.
    """

    def __init__(self, uid: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.uid = uid

        self.scanner_stub = scanner_pb2_grpc.ScannerStub(self.channel)
        self.exploit_stub = exploitation_pb2_grpc.ExploitServiceStub(
            self.channel
        )
        self.info_stub = information_pb2_grpc.InformationStub(self.channel)
        self.bloodhound_stub = bloodhound_pb2_grpc.BloodHoundStub(self.channel)
        self.relaying_stub = relaying_pb2_grpc.RelayingStub(self.channel)
        self.metasploit_stub = metasploit_pb2_grpc.MetasploitStub(self.channel)

    def get_info(self):
        """
            Get some generic info from the device like ip and version numbers.
        """
        return self.perform_request(
            self.info_stub.GetInfo,
            information_pb2.InfoRequest(filter=information_pb2.InfoRequest.ALL)
        )

    def get_settings(self):
        """
            Get the settings list.
        """
        return self.perform_request(self.info_stub.GetSettings, information_pb2.SettingsRequest())

    def set_setting(self, section, key, value):
        """
            Change a setting of a key to value.
        """
        section_pb2 = information_pb2.Section(name=section)
        setting_pb2 = section_pb2.settings.add()
        setting_pb2.key = key
        setting_pb2.value = value
        return self.perform_request(self.info_stub.SetSetting, section_pb2)

    def list_scans(self):
        """
            List all the scans
        """
        return self.perform_request(self.scanner_stub.ListScans, scanner_pb2.ScanListRequest())

    def create_scan(self, name: str, description: str, targets: List[str], ping: bool):
        """
            Create a new scan.
        """
        scan = models_pb2.Scan(name=name, description=description)
        for target in targets:
            pb_target = scan.targets.add()
            pb_target.address = target
            pb_target.ping = ping
        return self.perform_request(self.scanner_stub.CreateScan, scan)

    def add_targets(self, scan_id: int, targets: List[str], ping: bool):
        """
            Add new targets to an existing scan.
        """
        scan = models_pb2.Scan(id=scan_id)
        for target in targets:
            pb_target = scan.targets.add()
            pb_target.address = target
            pb_target.ping = ping
        return self.perform_request(self.scanner_stub.AddTargets, scan)

    def list_hosts(self, pagination: models_pb2.Pagination):
        """
            List the hosts with the given pagination.
        """
        return self.perform_request(self.scanner_stub.ListHosts, pagination)

    def list_host_filters(self, scan_id: int):
        return self.perform_request(
            self.scanner_stub.ListHostFilters,
            models_pb2.Scan(id=scan_id)
        )

    def get_host(self, host_id: int):
        """Retrieve a single host"""
        return self.perform_request(
            self.scanner_stub.GetHost,
            scanner_pb2.GetRequest(id=host_id)
        )

    def list_services(self, pagination: models_pb2.Pagination):
        return self.perform_request(self.scanner_stub.ListServices, pagination)

    def get_service(self, service_id: int):
        return self.perform_request(
            self.scanner_stub.GetService,
            scanner_pb2.GetRequest(id=service_id)
        )

    def list_service_filters(self, scan_id: int):
        return self.perform_request(
            self.scanner_stub.ListServiceFilters,
            models_pb2.Scan(id=scan_id)
        )

    def list_vulnerabilities(self, pagination: models_pb2.Pagination):
        return self.perform_request(self.scanner_stub.ListVulns, pagination)

    def list_vulnerability_filters(self, scan_id: int):
        return self.perform_request(
            self.scanner_stub.ListVulnFilters,
            models_pb2.Scan(id=scan_id)
        )

    def list_exploits(self, pagination: models_pb2.Pagination):
        return self.perform_request(self.scanner_stub.ListExploits, pagination)

    def get_exploit(self, exploit_id: int):
        return self.perform_request(
            self.scanner_stub.GetExploit,
            scanner_pb2.GetRequest(id=exploit_id)
        )

    def list_exploit_filters(self, scan_id: int):
        return self.perform_request(
            self.scanner_stub.ListExploitFilters,
            models_pb2.Scan(id=scan_id)
        )

    def list_credentials(self, pagination: models_pb2.Pagination):
        return self.perform_request(self.scanner_stub.ListCredentials, pagination)

    def get_credential(self, credential_id: int):
        return self.perform_request(
            self.scanner_stub.GetCredential,
            scanner_pb2.GetRequest(id=credential_id)
        )

    def list_credential_filters(self, scan_id: int):
        return self.perform_request(
            self.scanner_stub.ListCredentialFilters,
            models_pb2.Scan(id=scan_id)
        )

    def list_targets(self, pagination: models_pb2.Pagination):
        return self.perform_request(self.scanner_stub.ListTargets, pagination)

    def scan_stats(self, scan_id: int):
        return self.perform_request(self.scanner_stub.GetStats, models_pb2.Scan(id=scan_id))

    def list_loot_modules(self):
        return self.perform_request(self.exploit_stub.ListLootModules, models_pb2.EmptyRequest())

    def list_login_modules(self):
        return self.perform_request(self.exploit_stub.ListLoginModules, models_pb2.EmptyRequest())

    def exploit(self, vuln_id, exploit_id: str, credential_id: int):
        request = exploitation_pb2.ExploitRequest(
            vulnerability_id=vuln_id,
            exploit_id=exploit_id
        )
        if credential_id is not None:
            request.credential.CopyFrom(
                models_pb2.Credential(id=credential_id)
            )
        return self.perform_request(self.exploit_stub.PerformExploit, request)

    def list_loot(self, pagination: models_pb2.Pagination):
        return self.perform_request(self.scanner_stub.ListLoot, pagination)

    def get_loot(self, loot_id: int):
        return self.perform_request(
            self.scanner_stub.GetLoot,
            scanner_pb2.GetRequest(id=loot_id)
        )

    def list_loot_filters(self, scan_id: int):
        return self.perform_request(
            self.scanner_stub.ListLootFilters,
            models_pb2.Scan(id=scan_id)
        )

    def loot(self, service_id: int, credential_id: int, module_name: str):
        request = exploitation_pb2.LootRequest(
            service_id=service_id,
            credential_id=credential_id,
            module_name=module_name
        )
        return self.perform_request(self.exploit_stub.PerformLoot, request)

    def multi_loot(self, scan_id: int, credential_id: int, module_name: str, domain_id: int, port: int, max_number: int, not_looted: bool):
        request = exploitation_pb2.LootRequest(
            credential_id=credential_id,
            module_name=module_name,
            domain_id=domain_id,
            port=port,
            max_loot=max_number,
            only_not_looted=not_looted,
            scan_id=scan_id
        )
        return self.perform_request(self.exploit_stub.PerformMultipleLoot, request)

    def cancel_loot(self, loot_id: int = 0):
        request = exploitation_pb2.CancelRequest(
            id=loot_id,
        )
        return self.perform_request(self.exploit_stub.CancelLoot, request)

    def cancel_exploit(self, exploit_id: int = 0):
        request = exploitation_pb2.CancelRequest(
            id=exploit_id,
        )
        return self.perform_request(self.exploit_stub.CancelExploit, request)

    def list_discovery(self, pagination: models_pb2.Pagination):
        return self.perform_request(self.scanner_stub.ListDiscovery, pagination)

    def list_discovery_modules(self):
        return self.perform_request(self.scanner_stub.ListDiscoveryModules, models_pb2.EmptyRequest())

    def create_discovery(self, scan_id: int, ping: bool, modules: List[str]):
        discovery = models_pb2.Discovery(
            scan_id=scan_id,
            ping=ping,
            modules=modules
        )
        return self.perform_request(self.scanner_stub.StartDiscovery, discovery)

    def list_sessions(self, pagination: models_pb2.Pagination):
        return self.perform_request(self.scanner_stub.ListSession, pagination)

    def get_session(self, session_id: int):
        return self.perform_request(
            self.scanner_stub.GetSession,
            models_pb2.Scan(id=session_id)
        )

    def list_session_filters(self, scan_id: int):
        return self.perform_request(
            self.scanner_stub.ListSessionFilters,
            models_pb2.Scan(id=scan_id)
        )

    def list_local_admins(self, pagination: models_pb2.Pagination):
        return self.perform_request(self.scanner_stub.ListLocalAdmins, pagination)

    def get_local_admin(self, admin_id: int):
        return self.perform_request(
            self.scanner_stub.GetLocalAdmin,
            models_pb2.Scan(id=admin_id)
        )

    def list_local_admin_filters(self, scan_id: int):
        return self.perform_request(
            self.scanner_stub.ListLocalAdminFilters,
            models_pb2.Scan(id=scan_id)
        )

    def get_relaying_status(self):
        return self.perform_request(
            self.relaying_stub.GetStatus,
            relaying_pb2.RelayingRequest()
        )

    def list_relaying_targets(self, pagination: models_pb2.Pagination):
        return self.perform_request(
            self.scanner_stub.ListRelayingTargets,
            pagination
        )

    def list_relaying_log(self, pagination: models_pb2.Pagination):
        return self.perform_request(
            self.scanner_stub.ListRelayingLog,
            pagination
        )

    def start_responder(self, scan_id: int):
        return self.perform_request(
            self.relaying_stub.StartResponder,
            relaying_pb2.StartMessage(scan_id=scan_id)
        )

    def add_relaying_target(self, service_id: int):
        return self.perform_request(
            self.relaying_stub.AddRelayingTarget,
            models_pb2.RelayingTarget(service_id=service_id)
        )

    def start_mitm6(self, scan_id: int):
        return self.perform_request(
            self.relaying_stub.StartMitm6,
            relaying_pb2.StartMessage(scan_id=scan_id)
        )

    def start_relaying(self, scan_id: int):
        return self.perform_request(
            self.relaying_stub.StartRelaying,
            relaying_pb2.StartMessage(scan_id=scan_id)
        )

    def stop_responder(self, scan_id: int):
        return self.perform_request(
            self.relaying_stub.StopResponder,
            relaying_pb2.StopMessage()
        )

    def stop_mitm6(self, scan_id: int):
        return self.perform_request(
            self.relaying_stub.StopMitm6,
            relaying_pb2.StopMessage()
        )

    def stop_relaying(self, scan_id: int):
        return self.perform_request(
            self.relaying_stub.StopRelaying,
            relaying_pb2.StopMessage()
        )

    def start_all(self, scan_id: int):
        return self.perform_request(
            self.relaying_stub.StartAll,
            relaying_pb2.StartMessage(scan_id=scan_id)
        )

    def stop_all(self):
        return self.perform_request(
            self.relaying_stub.StopAll,
            relaying_pb2.StopMessage()
        )

    def get_responder_output(self):
        return self.perform_request(
            self.relaying_stub.GetResponderOutput,
            relaying_pb2.OutputRequest()
        )

    def get_mitm6_output(self):
        return self.perform_request(
            self.relaying_stub.GetMitm6Output,
            relaying_pb2.OutputRequest()
        )

    def get_relaying_output(self):
        return self.perform_request(
            self.relaying_stub.GetRelayingOutput,
            relaying_pb2.OutputRequest()
        )

    def list_files(self, pagination: models_pb2.Pagination):
        return self.perform_request(self.scanner_stub.ListFiles, pagination)

    def get_file(self, file_id: int):
        return self.perform_request(
            self.scanner_stub.GetFile,
            scanner_pb2.GetRequest(id=file_id)
        )

    def list_file_filters(self, scan_id: int):
        return self.perform_request(
            self.scanner_stub.ListFileFilters,
            models_pb2.Scan(id=scan_id)
        )

    def stream_image(self, file_id: int):
        for chunk in self.scanner_stub.GetFileStream(models_pb2.File(id=file_id)):
            yield chunk.chunk

    def add_credential(self, scan_id: int, username: str, password: str, domain: str, domain_id: int, lm: str, nt: str):
        credential = models_pb2.Credential(
            password=password, lm=lm, nt=nt, scan_id=scan_id
        )
        credential.user.MergeFrom(models_pb2.User(username=username))
        if domain or domain_id:
            credential.domain.MergeFrom(
                models_pb2.Domain(id=domain_id, dns_name=domain)
            )
        return self.perform_request(self.scanner_stub.AddCredential, credential)

    def list_out_of_scope(self, pagination: models_pb2.Pagination):
        return self.perform_request(
            self.scanner_stub.ListOutOfScope,
            pagination
        )

    def add_out_of_scope(self, scan_id: int, ip_range: str, description: str):
        return self.perform_request(
            self.scanner_stub.AddOutOfScope,
            models_pb2.OutOfScope(
                scan_id=scan_id,
                ip_range=ip_range,
                description=description)
        )

    def get_log(self, log_id: int):
        return self.perform_request(
            self.scanner_stub.GetLog,
            scanner_pb2.GetRequest(id=log_id)
        )

    def list_domains(self, pagination: models_pb2.Pagination):
        return self.perform_request(self.scanner_stub.ListDomains, pagination)

    def get_domain(self, domain_id: int):
        return self.perform_request(
            self.scanner_stub.GetDomain,
            scanner_pb2.GetRequest(id=domain_id)
        )

    def list_domain_filters(self, scan_id: int):
        return self.perform_request(
            self.scanner_stub.ListDomainFilters,
            models_pb2.Scan(id=scan_id)
        )

    def get_application_log(self, log_type: information_pb2.LogRequest.LogType, start: int, count: int):
        return self.perform_request(
            self.info_stub.GetLog,
            information_pb2.LogRequest(
                start=start,
                count=count,
                type=log_type
            )
        )

    def list_users(self, pagination: models_pb2.Pagination):
        return self.perform_request(self.scanner_stub.ListUsers, pagination)

    def get_user(self, user_id: int):
        return self.perform_request(
            self.scanner_stub.GetGroup,
            scanner_pb2.GetRequest(id=user_id)
        )

    def list_user_filters(self, scan_id: int):
        return self.perform_request(
            self.scanner_stub.ListUserFilters,
            models_pb2.Scan(id=scan_id)
        )

    def list_groups(self, pagination: models_pb2.Pagination):
        return self.perform_request(self.scanner_stub.ListGroups, pagination)

    def get_group(self, group_id: int):
        return self.perform_request(
            self.scanner_stub.GetGroup,
            scanner_pb2.GetRequest(id=group_id)
        )

    def list_group_filters(self, scan_id: int):
        return self.perform_request(
            self.scanner_stub.ListGroupFilters,
            models_pb2.Scan(id=scan_id)
        )

    def list_group_memberships(self, pagination: models_pb2.Pagination):
        return self.perform_request(self.scanner_stub.ListGroupMemberships, pagination)

    def get_group_membership(self, membership_id: int):
        return self.perform_request(
            self.scanner_stub.GetGroupMembership,
            scanner_pb2.GetRequest(id=membership_id)
        )

    def list_group_membership_filters(self, scan_id: int):
        return self.perform_request(
            self.scanner_stub.ListGroupMembershipFilters,
            models_pb2.Scan(id=scan_id)
        )

    def list_trusts(self, pagination: models_pb2.Pagination):
        return self.perform_request(self.scanner_stub.ListTrusts, pagination)

    def get_trust(self, trust_id: int):
        return self.perform_request(
            self.scanner_stub.GetTrust,
            scanner_pb2.GetRequest(id=trust_id)
        )

    def list_trust_filters(self, scan_id: int):
        return self.perform_request(
            self.scanner_stub.ListTrustFilters,
            models_pb2.Scan(id=scan_id)
        )

    def list_policies(self, pagination: models_pb2.Pagination):
        return self.perform_request(self.scanner_stub.ListPolicies, pagination)

    def get_policy(self, trust_id: int):
        return self.perform_request(
            self.scanner_stub.GetPolicy,
            scanner_pb2.GetRequest(id=trust_id)
        )

    def list_policy_filters(self, scan_id: int):
        return self.perform_request(
            self.scanner_stub.ListPolicyFilters,
            models_pb2.Scan(id=scan_id)
        )

    def list_hashes(self, pagination: models_pb2.Pagination):
        return self.perform_request(self.scanner_stub.ListHashes, pagination)

    def get_hash(self, hash_id: int):
        return self.perform_request(
            self.scanner_stub.GetHash,
            scanner_pb2.GetRequest(id=hash_id)
        )

    def list_hash_filters(self, scan_id: int):
        return self.perform_request(
            self.scanner_stub.ListHashFilters,
            models_pb2.Scan(id=scan_id)
        )

    # Bloodhound methods

    def list_domain_admin_groups(self, pagination: models_pb2.Pagination):
        return self.perform_request(self.bloodhound_stub.listDomainAdminGroups, pagination)

    def find_local_admins_for_user(self, scan_id: int, user_id: int):
        return self.perform_request(
            self.bloodhound_stub.findLocalAdminsForUser,
            bloodhound_pb2.BloodHoundRequest(
                scan_id=scan_id,
                user_id=user_id
            )
        )

    def find_path_to_domain_admins(self, scan_id: int, user_id: int):
        return self.perform_request(
            self.bloodhound_stub.findPathToDomainAdmin,
            bloodhound_pb2.BloodHoundRequest(
                scan_id=scan_id,
                user_id=user_id
            )
        )

    def find_all_paths_to_domain_admins(self, scan_id: int, domain_id: int):
        return self.perform_request(
            self.bloodhound_stub.findAllPathsToDomainAdmin,
            bloodhound_pb2.BloodHoundRequest(
                scan_id=scan_id,
                domain_id=domain_id
            )
        )

    def find_all_paths_to_da_from_creds(self, scan_id: int, domain_id: int):
        return self.perform_request(
            self.bloodhound_stub.findPathsToDAfromCreds,
            bloodhound_pb2.BloodHoundRequest(
                scan_id=scan_id,
                domain_id=domain_id
            )
        )

    def find_path(self, scan_id: int, from_id: int, from_type: str, to_id: int, to_type: str):
        from_node = bloodhound_pb2.Node()
        if from_type.lower() == 'user':
            from_node.user.MergeFrom(models_pb2.User(id=from_id))
        elif from_type.lower() == 'group':
            from_node.group.MergeFrom(models_pb2.Group(id=from_id))

        to_node = bloodhound_pb2.Node()
        if to_type.lower() == 'user':
            to_node.user.MergeFrom(models_pb2.User(id=to_id))
        elif to_type.lower() == 'group':
            to_node.group.MergeFrom(models_pb2.Group(id=to_id))

        path = bloodhound_pb2.FindPath()
        path.from_node.MergeFrom(from_node)
        path.to_node.MergeFrom(to_node)

        return self.perform_request(
            self.bloodhound_stub.findPath,
            bloodhound_pb2.BloodHoundRequest(
                path=path,
                scan_id=scan_id
            )
        )

    def loot_local_admins(self, scan_id: int, user_id: int, credential_id: int):
        return self.perform_request(
            self.bloodhound_stub.lootLocalAdmins,
            bloodhound_pb2.BloodHoundRequest(
                scan_id=scan_id,
                user_id=user_id,
                credential_id=credential_id
            )
        )

    def pwn_path(self, scan_id: int, user_id: int, credential_id: int, port: int, loot_module: str):
        return self.perform_request(
            self.bloodhound_stub.pwnPath,
            bloodhound_pb2.BloodHoundRequest(
                scan_id=scan_id,
                user_id=user_id,
                credential_id=credential_id,
                port=port,
                loot_module=loot_module)
        )

    def find_nodes(self, pagination: models_pb2.Pagination):
        return self.perform_request(
            self.bloodhound_stub.findNodes,
            pagination
        )

    def reload_graph_data(self, scan_id: int):
        return self.perform_request(
            self.bloodhound_stub.reloadGraphData,
            models_pb2.Scan(
                id=scan_id
            )
        )

    def get_graph_stats(self, scan_id: int):
        return self.perform_request(
            self.bloodhound_stub.getGraphStats,
            models_pb2.Scan(
                id=scan_id
            )
        )

    # metasploit functions

    def list_metasploit_consoles(self):
        return self.perform_request(
            self.metasploit_stub.ListConsoles,
            models_pb2.EmptyRequest()
        )

    def get_metasploit_console(self, id):
        return self.perform_request(
            self.metasploit_stub.GetConsole,
            metasploit_pb2.Console(
                id=id
            )
        )

    def create_metasploit_console(self):
        return self.perform_request(
            self.metasploit_stub.CreateConsole,
            models_pb2.EmptyRequest()
        )

    def stop_metasploit_console(self, cid: str):
        return self.perform_request(
            self.metasploit_stub.StopConsole,
            metasploit_pb2.Console(
                id=cid
            )
        )

    def write_to_console(self, cid: str, message: str):
        return self.perform_request(
            self.metasploit_stub.WriteToConsole,
            metasploit_pb2.ConsoleMessage(
                id=cid,
                message=message,
            )
        )

    def list_metasploit_sessions(self):
        return self.perform_request(
            self.metasploit_stub.ListSessions,
            models_pb2.EmptyRequest()
        )

    def get_metasploit_session(self, id: str):
        return self.perform_request(
            self.metasploit_stub.GetSession,
            metasploit_pb2.MetasploitSession(id=id)
        )

    def write_to_session(self, sid: str, message: str):
        return self.perform_request(
            self.metasploit_stub.WriteToSession,
            metasploit_pb2.ConsoleMessage(
                id=sid,
                message=message
            )
        )


class CallbackClient(Client):
    """
        CallbackClient implements functions to report results to a server.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.callback_stub = callback_pb2_grpc.CallbackServiceStub(self.channel)

    def new_host(self, host_id: int, scan_id: int, domain_id: int) -> None:
        self.perform_request(
            self.callback_stub.NewHost,
            callback_pb2.Callback(
                host_id=host_id,
                scan_id=scan_id,
                domain_id=domain_id
            )
        )

    def new_service(self, service_id: int, scan_id: int, host_id: int, port: int, domain_id: int) -> None:
        self.perform_request(
            self.callback_stub.NewService,
            callback_pb2.Callback(
                service_id=service_id,
                scan_id=scan_id,
                host_id=host_id,
                port=port,
                domain_id=domain_id,
            )
        )

    def new_vulnerability(self, vuln_id: int, scan_id: int, service_id: int,
                          exploit_ids: List[str], port: int, host_id: int, domain_id: int) -> None:
        self.perform_request(
            self.callback_stub.NewService,
            callback_pb2.Callback(
                vuln_id=vuln_id,
                scan_id=scan_id,
                service_id=service_id,
                exploit_ids=exploit_ids,
                port=port,
                host_id=host_id,
                domain_id=domain_id,
            )
        )

    def new_user(self, user_id: int, scan_id: int) -> None:
        self.perform_request(
            self.callback_stub.NewService,
            callback_pb2.Callback(
                user_id=user_id,
                scan_id=scan_id,
            )
        )

    def new_credential(self, credential_id: int, scan_id: int, domain_id: int) -> None:
        self.perform_request(
            self.callback_stub.NewService,
            callback_pb2.Callback(
                credential_id=credential_id,
                scan_id=scan_id,
                domain_id=domain_id,
            )
        )

    def new_domain(self, scan_id: int, domain_id: int) -> None:
        self.perform_request(
            self.callback_stub.NewService,
            callback_pb2.Callback(
                domain_id=domain_id,
                scan_id=scan_id,
            )
        )

    def console_output(self, cid: str, output: str, prompt: str) -> None:
        """Report console output to the server"""
        self.perform_request(
            self.callback_stub.NewConsoleOutput,
            metasploit_pb2.ConsoleOutput(
                cid=cid,
                output=output,
                prompt=prompt,
            )
        )


    def session_output(self, sid: str, message: str) -> None:
        """Report session message to the server"""
        self.perform_request(
            self.callback_stub.NewSessionOutput,
            metasploit_pb2.SessionOutput(
                sid=sid,
                message=message,
            )
        )


class WireguardClient(Client):
    """
        Client to communicate with the wireguard grpc server.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.wireguard_stub = wireguard_pb2_grpc.WireguardStub(self.channel)

    def generate_key(self):
        """Generate a public / private key combination"""
        return self.perform_request(
            self.wireguard_stub.GenKey,
            models_pb2.EmptyMessage()
        )

    def add_peer(self, public_key: str, allowed_ips: List[str]):
        """Add a peer to the server"""
        peer = wireguard_pb2.Peer(
            public_key=public_key,
            allowed_ips=[wireguard_pb2.IP(ip=ip) for ip in allowed_ips]
        )
        return self.perform_request(
            self.wireguard_stub.AddPeer,
            peer
        )

    def remove_peer(self, public_key: str):
        """Remove a peer from the server"""
        peer = wireguard_pb2.Peer(
            public_key=public_key
        )
        return self.perform_request(
            self.wireguard_stub.RemovePeer,
            peer
        )

    def list_peers(self):
        """List the current peers of the server"""
        return self.perform_request(
            self.wireguard_stub.ListPeers,
            models_pb2.EmptyRequest()
        )

    def get_interface(self):
        """Get the interface of the server"""
        return self.perform_request(
            self.wireguard_stub.GetInterface,
            models_pb2.EmptyRequest()
        )
