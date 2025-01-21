### Introduction

I am currently working as a Cloud Networking Specialist @ Microsoft. Therefore you will find most of the content related to Azure Networking.

### Azure

- NVAs in Azure
   - [OPNsense NVA Firewall in Azure](https://github.com/dmauser/opnazure)
   - [Deploy Linux or Windows VM as routers (IPv4/IPv6/NAT2Internet)](https://github.com/dmauser/AzureVM-Router)

- Azure Virtual Network
   - [LAB:Azure Virtual Network Encryption](https://github.com/dmauser/azure-vnet-encryption)

- Azure VMWare Solution (AVS)
   - [LAB: AVS (ER) to On-prem (ER) transit using Secured-vHub+Routing Intent](https://github.com/dmauser/azure-vmware-solution)

- [Azure Site-to-Site VPN](https://github.com/dmauser/azure-vpn-s2s)
  - [Verify BGP information on Azure VPN and ExpressRoute Gateways](https://github.com/dmauser/Lab/tree/master/ER-and-VPN-Gateway-BGP-info)
  - [Troubleshooting IPSec by using IKE Logs](https://github.com/dmauser/Lab/tree/master/VPN-gateway-IKE-logs)
  - [Site-to-Site VPN between Azure and GCP (static routing)](https://github.com/dmauser/azure-vpn-s2s-gcp)
  - [LAB: NAT on Azure VPN Gateway](https://github.com/dmauser/azure-vpn-s2s-nat) 
  - [LAB: Transit between ExpressRoute and Azure S2S VPN using Route Server](https://github.com/dmauser/Lab/tree/master/RS-ER-VPN-Gateway-Transit)
  - [LAB: Using Azure Firewall to inspect traffic between VPN and ExpressRoute](https://github.com/dmauser/Lab/tree/master/RS-ER-VPN-Gateway-Transit-AzFW)
  - [Powershell script: Azure Virtual Network Gateway Packet Capture](https://github.com/dmauser/Lab/tree/master/VPN-gateway-packet-capture) 
  - [LAB: GCP Site-to-Site VPN with Azure](https://github.com/dmauser/azure-vpn-s2s-gcp)

- [Azure ExpressRoute](https://github.com/dmauser/azure-expressroute)
  - [Transit between ExpressRoute circuits](https://github.com/dmauser/azure-expressroute/tree/main/er-to-er-transit)
    - [LAB: Transit between ExpressRoute circuits using NVAs/ARS (reverse hairpin)](https://github.com/dmauser/azure-expressroute/tree/main/er-to-er-transit/ars/lab) 
  - [Deploying Local SKU ExpressRoute Circuits](https://github.com/dmauser/Lab/tree/master/ExpressRoute-local)
  - [LAB: Azure VPN/ER Coexistence using GCP as On-premises](https://github.com/dmauser/azure-er-vpn-coexistence)
  - [LAB: Verify BGP information on Azure VPN and ExpressRoute Gateways](https://github.com/dmauser/Lab/tree/master/ER-and-VPN-Gateway-BGP-info)

- [Azure Gateway Load Balancer](https://github.com/dmauser/azure-gateway-lb)

- [Azure Virtual WAN (VWAN)](https://github.com/dmauser/azure-virtualwan)
  - [Multiple Virtual WANs (Prod and Dev)](https://github.com/dmauser/Lab/tree/master/vWAN-split-dev-and-prod-design)
  - [vWAN VPN Gateway Packet Capture](https://github.com/dmauser/Lab/tree/master/vWAN-vpn-gateway-packet-capture)
  - [Sample script showing how to migrate Spoke VNET from traditional HUB/Spoke to vWAN HUB](https://github.com/dmauser/Lab/tree/master/vWAN-spoke-vnet-sample-migration-script)
  - [Azure Virtual Network Gateway IKE Logs](https://github.com/dmauser/Lab/tree/master/VPN-gateway-IKE-logs)
  - [LAB: Virtual WAN scenario: any-to-any](https://github.com/dmauser/azure-virtualwan/tree/main/any-to-any)
  - [LAB: Virtual WAN scenario: Route traffic through an Azure Firewall spoke](https://github.com/dmauser/azure-virtualwan/tree/main/inter-region-azfw)
  - [LAB: Virtual WAN scenario: Route traffic through an NVA spoke](https://github.com/dmauser/azure-virtualwan/tree/main/inter-region-nva)
  - [LAB: Virtual WAN scenario: Route traffic through an NVA spoke using BGP Peering](https://github.com/dmauser/azure-virtualwan/tree/main/inter-region-nvabgp)
  - [LAB: Virtual WAN scenario: Isolated VNETs using custom route tables](https://github.com/dmauser/azure-virtualwan/tree/main/isolate-vnets-custom)
  - [LAB: Azure Virtual WAN scenario: using NVA on Spoke for Internet](https://github.com/dmauser/azure-virtualwan/tree/main/nva-spoke-internet)
  - [Script to dump all vHUBs effective routes](https://github.com/dmauser/azure-virtualwan/tree/main/misc-cheatsheet#script-to-dump-all-vhubs-effective-routes)
  - [LAB: Secured Virtual Hubs and Routing Intent (Intra-Region)](https://github.com/dmauser/azure-virtualwan/tree/main/svh-ri-intra-region)
  - [LAB: Secured Virtual Hubs Inter-region via ExpressRoute](https://github.com/dmauser/azure-virtualwan/tree/main/svh-inter-region-er)
  - [LAB: Virtual WAN Scenario: IPsec VPN over ER](https://github.com/dmauser/azure-virtualwan/tree/main/vpn-over-er)
  - [LAB: Virtual WAN Scenario: IPsec VPN with NAT over ER](https://github.com/dmauser/azure-virtualwan/tree/main/natvpn-over-er)
  - [LAB: Virtual WAN and forced tunneling over ExpressRoute](https://github.com/dmauser/azure-virtualwan/tree/main/ft-wan)
  
- [Private Link](https://github.com/dmauser/PrivateLink)
   - [Private Endpoint DNS Integration Scenarios](https://github.com/dmauser/PrivateLink/tree/master/DNS-Integration-Scenarios)
   - [Known Issue: Azure Customers are unable to access each other PaaS Resources when both sides are exposed to PrivateLink/Endpoint](https://github.com/dmauser/PrivateLink/tree/master/Issue-Customer-Unable-to-Access-PaaS-AfterPrivateLink)
   - [DNS Client Configuration Options for Private Endpoints](https://github.com/dmauser/PrivateLink/tree/master/DNS-Client-Configuration-Options)
   - [Private Endpoint DNS integration using Active Directory](https://github.com/dmauser/PrivateLink/tree/master/DNS-Scenario-Using-AD)
   - [Private Endpoint DNS integration over Point to Site VPN connection](https://github.com/dmauser/PrivateLink/tree/master/DNS-Integration-P2S)
   - [Using Private Link Service for On-premises workloads](https://github.com/dmauser/PrivateLink/tree/master/PLS-for-Onprem-workloads)
     - [LAB: Using Private Link Service to publish On-premises workloads by using HAProxy](https://github.com/dmauser/Lab/tree/master/PLS-for-onprem-workloads-haproxy)
   - [Network performance considerations when using Azure Files over Private Endpoint](https://github.com/dmauser/azure-files-netperf)

- Azure Files
  - [Network performance considerations when using Azure Files over Private Endpoint](https://github.com/dmauser/azure-files-netperf)
    
- [Azure Route Server](https://github.com/dmauser/azure-routeserver)
   - [Forced Tunneling of Internet traffic through Active-Active OPNsense Firewalls using Azure Route Server (ExpressRoute)](https://github.com/dmauser/Lab/tree/master/RS-AA-OPNsense-ForceTunnel-ER)
   - [Transit between ExpressRoute and Azure S2S VPN using Route Server](https://github.com/dmauser/Lab/tree/master/RS-ER-VPN-Gateway-Transit)
   - [Using Azure Firewall to inspect traffic between VPN and ExpressRoute](https://github.com/dmauser/Lab/tree/master/RS-ER-VPN-Gateway-Transit-AzFW)
   - [LAB: Transit between ExpressRoute circuits using NVAs/ARS (reverse hairpin)](https://github.com/dmauser/azure-expressroute/tree/main/er-to-er-transit/ars/lab)
   - [LAB: High Available NVAs with Azure Route Server](https://github.com/dmauser/azure-routeserver/tree/main/ars-nhip)

- Azure Firewall
  - [LAB: Using Azure Firewall to inspect traffic between VPN and ExpressRoute](https://github.com/dmauser/Lab/tree/master/RS-ER-VPN-Gateway-Transit-AzFW)
  - [LAB: Virtual WAN scenario: Route traffic through an Azure Firewall spoke](https://github.com/dmauser/azure-virtualwan/tree/main/inter-region-azfw)
  - [LAB: Secured Virtual Hubs and Routing Intent (Intra-Region)](https://github.com/dmauser/azure-virtualwan/tree/main/nva-spoke-internet)
  - [LAB: Secured Virtual Hubs Inter-region via ExpressRoute](https://github.com/dmauser/azure-virtualwan/tree/main/svh-inter-region-er)
  
- [Azure DNS Private Resolver](https://github.com/dmauser/azure-dns-private-resolver)
  - [Lab: Azure DNS Private Resolver (Hub and Spoke)](https://github.com/dmauser/azure-dns-private-resolver/tree/main/adr-lab)

- [Running DHCP Server on Azure VM](https://github.com/dmauser/DHCPServer-On-Azure)

- [Random_Scripts@GitHubGist](https://gist.github.com/dmauser)

### GCP
- [GCP base Networking Lab](https://github.com/dmauser/gcp-network-base-lab)
- [LAB: GCP Site-to-Site VPN with Azure](https://github.com/dmauser/azure-vpn-s2s-gcp)

## Other recommended Github repos on Cloud Newtworking

Recommended GitHub repos to check out with relevant Azure Networking content:

- https://github.com/fabferri
- https://github.com/paolosalvatori
- https://github.com/jocortems
- https://github.com/erjosito
- https://github.com/adstuart
- https://github.com/jwrightazure
- https://github.com/jtracey93
- https://github.com/fguerri
- https://github.com/hsze
- https://github.com/mddazure

<h2>⭐ GitHub Stats</h2>

[![Mauser's GitHub Stats](https://github-readme-stats.vercel.app/api?username=dmauser&show_icons=true)](https://github.com/dmauser)

