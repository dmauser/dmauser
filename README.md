### Introduction

Cloud Networking Specialist at Microsoft. Most content here is focused on **Azure Networking** — labs, scripts, and reference implementations covering VPN, ExpressRoute, Virtual WAN, Private Link, NVAs, and more.

---

## Table of Contents

- [Azure](#azure)
  - [NVAs in Azure](#nvas-in-azure)
  - [Azure Front Door](#azure-front-door)
  - [Azure Virtual Network](#azure-virtual-network)
  - [Azure VMware Solution (AVS)](#azure-vmware-solution-avs)
  - [Azure Site-to-Site VPN](#azure-site-to-site-vpn)
  - [Azure ExpressRoute](#azure-expressroute)
  - [Azure Gateway Load Balancer](#azure-gateway-load-balancer)
  - [Azure Virtual WAN (VWAN)](#azure-virtual-wan-vwan)
  - [Private Link](#private-link)
  - [Azure Files](#azure-files)
  - [Azure Route Server](#azure-route-server)
  - [Azure Firewall](#azure-firewall)
  - [Azure DNS Private Resolver](#azure-dns-private-resolver)
  - [Running DHCP Server on Azure](#running-dhcp-server-on-azure)
  - [Random Scripts](#random-scripts)
- [GCP](#gcp)
- [Other Recommended Repos](#other-recommended-github-repos-on-cloud-networking)

---

### Azure

#### NVAs in Azure

- [OPNsense NVA Firewall in Azure](https://github.com/dmauser/opnazure) *(Last updated: Mar 2026)*
- [Deploy Linux or Windows VM as Routers (IPv4/IPv6/NAT)](https://github.com/dmauser/AzureVM-Router) *(Last updated: Jan 2026)*

#### Azure Front Door

- [LAB: Azure Front Door and Private Link Service](https://github.com/dmauser/azure-frontdoor-pls) *(Last updated: Sep 2025)*

#### Azure Virtual Network

- [LAB: Azure Virtual Network Encryption](https://github.com/dmauser/azure-vnet-encryption) *(Last updated: Feb 2026)*

#### Azure VMware Solution (AVS)

- [LAB: AVS (ER) to On-prem (ER) Transit using Secured vHub + Routing Intent](https://github.com/dmauser/azure-vmware-solution) *(Last updated: Jun 2025)*

#### Azure Site-to-Site VPN

- [Azure Site-to-Site VPN](https://github.com/dmauser/azure-vpn-s2s) *(Last updated: Jul 2024)*
  - [Verify BGP Information on Azure VPN and ExpressRoute Gateways](https://github.com/dmauser/Lab/tree/master/ER-and-VPN-Gateway-BGP-info)
  - [Troubleshooting IPSec by Using IKE Logs](https://github.com/dmauser/Lab/tree/master/VPN-gateway-IKE-logs)
  - [Site-to-Site VPN between Azure and GCP (static routing)](https://github.com/dmauser/azure-vpn-s2s-gcp) *(Last updated: Jan 2022)*
  - [LAB: NAT on Azure VPN Gateway](https://github.com/dmauser/azure-vpn-s2s-nat) *(Last updated: May 2025)*
  - [LAB: Transit between ExpressRoute and Azure S2S VPN using Route Server](https://github.com/dmauser/Lab/tree/master/RS-ER-VPN-Gateway-Transit)
  - [LAB: Azure Firewall to Inspect Traffic between VPN and ExpressRoute](https://github.com/dmauser/Lab/tree/master/RS-ER-VPN-Gateway-Transit-AzFW)
  - [PowerShell: Azure Virtual Network Gateway Packet Capture](https://github.com/dmauser/Lab/tree/master/VPN-gateway-packet-capture)

> Sub-items above are part of [dmauser/Lab](https://github.com/dmauser/Lab) *(Last updated: Nov 2024)*

#### Azure ExpressRoute

- [Azure ExpressRoute](https://github.com/dmauser/azure-expressroute) *(Last updated: Apr 2024)*
  - [Transit between ExpressRoute Circuits](https://github.com/dmauser/azure-expressroute/tree/main/er-to-er-transit)
    - [LAB: ER-to-ER Transit using NVAs/ARS (reverse hairpin)](https://github.com/dmauser/azure-expressroute/tree/main/er-to-er-transit/ars/lab)
  - [Deploying Local SKU ExpressRoute Circuits](https://github.com/dmauser/Lab/tree/master/ExpressRoute-local)
  - [LAB: Azure VPN/ER Coexistence using GCP as On-premises](https://github.com/dmauser/azure-er-vpn-coexistence) *(Last updated: Apr 2024)*
  - [LAB: Verify BGP Information on Azure VPN and ExpressRoute Gateways](https://github.com/dmauser/Lab/tree/master/ER-and-VPN-Gateway-BGP-info)

#### Azure Gateway Load Balancer

- [Azure Gateway Load Balancer](https://github.com/dmauser/azure-gateway-lb) *(Last updated: Feb 2025)*

#### Azure Virtual WAN (VWAN)

- [Azure Virtual WAN](https://github.com/dmauser/azure-virtualwan) *(Last updated: Jun 2025)*
  - [LAB: Validating Virtual WAN Next Hop IP Feature](https://github.com/dmauser/azure-virtualwan-nexthop) *(Last updated: Jun 2025)*
  - [Multiple Virtual WANs (Prod and Dev)](https://github.com/dmauser/Lab/tree/master/vWAN-split-dev-and-prod-design)
  - [vWAN VPN Gateway Packet Capture](https://github.com/dmauser/Lab/tree/master/vWAN-vpn-gateway-packet-capture)
  - [Sample Script: Migrate Spoke VNET from Hub/Spoke to vWAN](https://github.com/dmauser/Lab/tree/master/vWAN-spoke-vnet-sample-migration-script)
  - [Azure Virtual Network Gateway IKE Logs](https://github.com/dmauser/Lab/tree/master/VPN-gateway-IKE-logs)
  - [LAB: Virtual WAN — Any-to-Any](https://github.com/dmauser/azure-virtualwan/tree/main/any-to-any)
  - [LAB: Route Traffic Through Azure Firewall Spoke](https://github.com/dmauser/azure-virtualwan/tree/main/inter-region-azfw)
  - [LAB: Route Traffic Through NVA Spoke](https://github.com/dmauser/azure-virtualwan/tree/main/inter-region-nva)
  - [LAB: Route Traffic Through NVA Spoke using BGP Peering](https://github.com/dmauser/azure-virtualwan/tree/main/inter-region-nvabgp)
  - [LAB: Isolated VNETs using Custom Route Tables](https://github.com/dmauser/azure-virtualwan/tree/main/isolate-vnets-custom)
  - [LAB: NVA on Spoke for Internet Breakout](https://github.com/dmauser/azure-virtualwan/tree/main/nva-spoke-internet)
  - [Script: Dump All vHUBs Effective Routes](https://github.com/dmauser/azure-virtualwan/tree/main/misc-cheatsheet#script-to-dump-all-vhubs-effective-routes)
  - [LAB: Secured Virtual Hubs and Routing Intent (Intra-Region)](https://github.com/dmauser/azure-virtualwan/tree/main/svh-ri-intra-region)
  - [LAB: Secured Virtual Hubs Inter-region via ExpressRoute](https://github.com/dmauser/azure-virtualwan/tree/main/svh-inter-region-er)
  - [LAB: IPsec VPN over ExpressRoute](https://github.com/dmauser/azure-virtualwan/tree/main/vpn-over-er)
  - [LAB: IPsec VPN with NAT over ExpressRoute](https://github.com/dmauser/azure-virtualwan/tree/main/natvpn-over-er)
  - [LAB: Forced Tunneling over ExpressRoute](https://github.com/dmauser/azure-virtualwan/tree/main/ft-wan)

> Some sub-items above are part of [dmauser/Lab](https://github.com/dmauser/Lab) *(Last updated: Nov 2024)*

#### Private Link

- [Private Link](https://github.com/dmauser/PrivateLink) *(Last updated: Feb 2025)*
  - [Private Endpoint DNS Integration Scenarios](https://github.com/dmauser/PrivateLink/tree/master/DNS-Integration-Scenarios)
  - [Known Issue: Customers Unable to Access Each Other's PaaS Resources after PrivateLink](https://github.com/dmauser/PrivateLink/tree/master/Issue-Customer-Unable-to-Access-PaaS-AfterPrivateLink)
  - [DNS Client Configuration Options for Private Endpoints](https://github.com/dmauser/PrivateLink/tree/master/DNS-Client-Configuration-Options)
  - [Private Endpoint DNS Integration using Active Directory](https://github.com/dmauser/PrivateLink/tree/master/DNS-Scenario-Using-AD)
  - [Private Endpoint DNS Integration over Point-to-Site VPN](https://github.com/dmauser/PrivateLink/tree/master/DNS-Integration-P2S)
  - [Using Private Link Service for On-premises Workloads](https://github.com/dmauser/PrivateLink/tree/master/PLS-for-Onprem-workloads)
    - [LAB: Publish On-premises Workloads using Private Link Service + HAProxy](https://github.com/dmauser/Lab/tree/master/PLS-for-onprem-workloads-haproxy)
  - [Network Performance Considerations: Azure Files over Private Endpoint](https://github.com/dmauser/azure-files-netperf)

#### Azure Files

- [Network Performance Considerations when Using Azure Files over Private Endpoint](https://github.com/dmauser/azure-files-netperf) *(Last updated: Oct 2021)*

#### Azure Route Server

- [Azure Route Server](https://github.com/dmauser/azure-routeserver) *(Last updated: Oct 2024)*
  - [Forced Tunneling: Active-Active OPNsense Firewalls with Route Server (ExpressRoute)](https://github.com/dmauser/Lab/tree/master/RS-AA-OPNsense-ForceTunnel-ER)
  - [Transit between ExpressRoute and Azure S2S VPN using Route Server](https://github.com/dmauser/Lab/tree/master/RS-ER-VPN-Gateway-Transit)
  - [Azure Firewall to Inspect Traffic between VPN and ExpressRoute](https://github.com/dmauser/Lab/tree/master/RS-ER-VPN-Gateway-Transit-AzFW)
  - [LAB: ER-to-ER Transit using NVAs/ARS (reverse hairpin)](https://github.com/dmauser/azure-expressroute/tree/main/er-to-er-transit/ars/lab)
  - [LAB: High Available NVAs with Azure Route Server](https://github.com/dmauser/azure-routeserver/tree/main/ars-nhip)

#### Azure Firewall

- [LAB: Azure Firewall to Inspect Traffic between VPN and ExpressRoute](https://github.com/dmauser/Lab/tree/master/RS-ER-VPN-Gateway-Transit-AzFW)
- [LAB: Virtual WAN — Route Traffic Through Azure Firewall Spoke](https://github.com/dmauser/azure-virtualwan/tree/main/inter-region-azfw)
- [LAB: Secured Virtual Hubs and Routing Intent (Intra-Region)](https://github.com/dmauser/azure-virtualwan/tree/main/nva-spoke-internet)
- [LAB: Secured Virtual Hubs Inter-region via ExpressRoute](https://github.com/dmauser/azure-virtualwan/tree/main/svh-inter-region-er)

#### Azure DNS Private Resolver

- [Azure DNS Private Resolver](https://github.com/dmauser/azure-dns-private-resolver) *(Last updated: Jan 2026)*
  - [LAB: Azure DNS Private Resolver — Hub and Spoke](https://github.com/dmauser/azure-dns-private-resolver/tree/main/adr-lab)

#### Running DHCP Server on Azure

- [Running DHCP Server on Azure VM](https://github.com/dmauser/DHCPServer-On-Azure) *(Last updated: May 2024)*

#### Random Scripts

- [Random Scripts @ GitHub Gist](https://gist.github.com/dmauser)

---

### GCP

- [GCP Base Networking Lab](https://github.com/dmauser/gcp-network-base-lab) *(Last updated: Sep 2022)*
- [LAB: GCP Site-to-Site VPN with Azure](https://github.com/dmauser/azure-vpn-s2s-gcp) *(Last updated: Jan 2022)*

---
## Other Recommended GitHub Repos on Cloud Networking

Community repositories with great Azure Networking content:

| GitHub | Profile |
|--------|---------|
| [@fabferri](https://github.com/fabferri) | https://github.com/fabferri |
| [@paolosalvatori](https://github.com/paolosalvatori) | https://github.com/paolosalvatori |
| [@jocortems](https://github.com/jocortems) | https://github.com/jocortems |
| [@erjosito](https://github.com/erjosito) | https://github.com/erjosito |
| [@adstuart](https://github.com/adstuart) | https://github.com/adstuart |
| [@jwrightazure](https://github.com/jwrightazure) | https://github.com/jwrightazure |
| [@jtracey93](https://github.com/jtracey93) | https://github.com/jtracey93 |
| [@fguerri](https://github.com/fguerri) | https://github.com/fguerri |
| [@hsze](https://github.com/hsze) | https://github.com/hsze |
| [@mddazure](https://github.com/mddazure) | https://github.com/mddazure |

---