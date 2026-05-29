<h1 align="center">🌐 Daniel Mauser</h1>

<p align="center">
  <b>Cloud Networking Specialist @ Microsoft</b><br>
  Labs, scripts, and reference implementations for <b>Azure Networking</b> — VPN, ExpressRoute, Virtual WAN, Private Link, NVAs, and more.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Microsoft-Cloud%20Networking-0078D4?logo=microsoft&logoColor=white" alt="Microsoft Cloud Networking">
  <img src="https://img.shields.io/badge/Azure-Networking-0089D6?logo=microsoftazure&logoColor=white" alt="Azure Networking">
  <a href="https://www.linkedin.com/in/danmauser/"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://gist.github.com/dmauser"><img src="https://img.shields.io/badge/GitHub-Gists-181717?logo=github&logoColor=white" alt="GitHub Gists"></a>
</p>

---

## About

I focus on **Azure networking** — designing, testing, and documenting connectivity, routing, security,
and hybrid scenarios. This profile is a curated index of hands-on **labs, sample scripts, and reference
implementations** I maintain across multiple repositories. Most content is reproducible end-to-end so you
can deploy, break, and learn from real Azure topologies.

📫 **Connect:** [LinkedIn](https://www.linkedin.com/in/danmauser/) · [GitHub Gists](https://gist.github.com/dmauser)

---

## 📑 Table of Contents

- [Featured](#featured)
- [Tools & Extensions](#tools--extensions)
- [Hybrid Connectivity (VPN & ExpressRoute)](#hybrid-connectivity-vpn--expressroute)
- [Virtual WAN](#virtual-wan)
- [Routing, Route Server & NVAs](#routing-route-server--nvas)
- [Private Link & DNS](#private-link--dns)
- [Firewall & Network Security](#firewall--network-security)
- [Core Networking & Edge](#core-networking--edge)
- [GCP & Multi-Cloud](#gcp--multi-cloud)
- [Recommended Repos](#recommended-repos)
- [GitHub Statistics](#github-statistics)

---

## Featured

- [Network Desk — GitHub Copilot CLI extension pack (20 cloud-networking specialist agents)](https://github.com/dmauser/network-desk) *(Last updated: May 2026)*
- [OPNsense NVA Firewall in Azure](https://github.com/dmauser/opnazure) *(Last updated: Mar 2026)*
- [Deploy Linux or Windows VM as Routers (IPv4/IPv6/NAT)](https://github.com/dmauser/AzureVM-Router) *(Last updated: Jan 2026)*
- [LAB: Azure DNS Security Policy](https://github.com/dmauser/AzDnsSecurityPolicyLab) *(Last updated: Mar 2026)*
- [LAB: Azure Virtual Network Encryption](https://github.com/dmauser/azure-vnet-encryption) *(Last updated: Feb 2026)*

---

## Tools & Extensions

- [Network Desk](https://github.com/dmauser/network-desk) — GitHub Copilot CLI extension pack: 20 specialist AI agents for cloud networking (Azure/AWS/GCP), firewalls (14 vendors), and report generation *(Last updated: May 2026)*

---

## Hybrid Connectivity (VPN & ExpressRoute)

### Azure Site-to-Site VPN

- [Azure Site-to-Site VPN](https://github.com/dmauser/azure-vpn-s2s) *(Last updated: Jul 2024)*
  - [Verify BGP Information on Azure VPN and ExpressRoute Gateways](https://github.com/dmauser/Lab/tree/master/ER-and-VPN-Gateway-BGP-info)
  - [Troubleshooting IPSec by Using IKE Logs](https://github.com/dmauser/Lab/tree/master/VPN-gateway-IKE-logs)
  - [Site-to-Site VPN between Azure and GCP (static routing)](https://github.com/dmauser/azure-vpn-s2s-gcp) *(Last updated: Jan 2022)*
  - [LAB: NAT on Azure VPN Gateway](https://github.com/dmauser/azure-vpn-s2s-nat) *(Last updated: May 2025)*
  - [LAB: Transit between ExpressRoute and Azure S2S VPN using Route Server](https://github.com/dmauser/Lab/tree/master/RS-ER-VPN-Gateway-Transit)
  - [LAB: Azure Firewall to Inspect Traffic between VPN and ExpressRoute](https://github.com/dmauser/Lab/tree/master/RS-ER-VPN-Gateway-Transit-AzFW)
  - [PowerShell: Azure Virtual Network Gateway Packet Capture](https://github.com/dmauser/Lab/tree/master/VPN-gateway-packet-capture)

> Sub-items above are part of [dmauser/Lab](https://github.com/dmauser/Lab) *(Last updated: Nov 2024)*

### Azure ExpressRoute

- [Azure ExpressRoute](https://github.com/dmauser/azure-expressroute) *(Last updated: Apr 2024)*
  - [Transit between ExpressRoute Circuits](https://github.com/dmauser/azure-expressroute/tree/main/er-to-er-transit)
    - [LAB: ER-to-ER Transit using NVAs/ARS (reverse hairpin)](https://github.com/dmauser/azure-expressroute/tree/main/er-to-er-transit/ars/lab)
  - [Deploying Local SKU ExpressRoute Circuits](https://github.com/dmauser/Lab/tree/master/ExpressRoute-local)
  - [LAB: Azure VPN/ER Coexistence using GCP as On-premises](https://github.com/dmauser/azure-er-vpn-coexistence) *(Last updated: Apr 2024)*
  - [LAB: Verify BGP Information on Azure VPN and ExpressRoute Gateways](https://github.com/dmauser/Lab/tree/master/ER-and-VPN-Gateway-BGP-info)

---

## Virtual WAN

<details>
<summary><b>Azure Virtual WAN (VWAN) — labs & scripts</b> <i>(Last updated: Jun 2025)</i></summary>

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

</details>

---

## Routing, Route Server & NVAs

### Azure Route Server

- [Azure Route Server](https://github.com/dmauser/azure-routeserver) *(Last updated: Oct 2024)*
  - [Forced Tunneling: Active-Active OPNsense Firewalls with Route Server (ExpressRoute)](https://github.com/dmauser/Lab/tree/master/RS-AA-OPNsense-ForceTunnel-ER)
  - [Transit between ExpressRoute and Azure S2S VPN using Route Server](https://github.com/dmauser/Lab/tree/master/RS-ER-VPN-Gateway-Transit)
  - [Azure Firewall to Inspect Traffic between VPN and ExpressRoute](https://github.com/dmauser/Lab/tree/master/RS-ER-VPN-Gateway-Transit-AzFW)
  - [LAB: ER-to-ER Transit using NVAs/ARS (reverse hairpin)](https://github.com/dmauser/azure-expressroute/tree/main/er-to-er-transit/ars/lab)
  - [LAB: High Available NVAs with Azure Route Server](https://github.com/dmauser/azure-routeserver/tree/main/ars-nhip)

### NVAs & Load Balancing

- [OPNsense NVA Firewall in Azure](https://github.com/dmauser/opnazure) *(Last updated: Mar 2026)*
- [Deploy Linux or Windows VM as Routers (IPv4/IPv6/NAT)](https://github.com/dmauser/AzureVM-Router) *(Last updated: Jan 2026)*
- [Azure Gateway Load Balancer](https://github.com/dmauser/azure-gateway-lb) *(Last updated: Feb 2025)*

---

## Private Link & DNS

<details>
<summary><b>Private Link — DNS integration scenarios & known issues</b> <i>(Last updated: Feb 2025)</i></summary>

- [Private Link](https://github.com/dmauser/PrivateLink) *(Last updated: Feb 2025)*
  - [Private Endpoint DNS Integration Scenarios](https://github.com/dmauser/PrivateLink/tree/master/DNS-Integration-Scenarios)
  - [Known Issue: Customers Unable to Access Each Other's PaaS Resources after PrivateLink](https://github.com/dmauser/PrivateLink/tree/master/Issue-Customer-Unable-to-Access-PaaS-AfterPrivateLink)
  - [DNS Client Configuration Options for Private Endpoints](https://github.com/dmauser/PrivateLink/tree/master/DNS-Client-Configuration-Options)
  - [Private Endpoint DNS Integration using Active Directory](https://github.com/dmauser/PrivateLink/tree/master/DNS-Scenario-Using-AD)
  - [Private Endpoint DNS Integration over Point-to-Site VPN](https://github.com/dmauser/PrivateLink/tree/master/DNS-Integration-P2S)
  - [Using Private Link Service for On-premises Workloads](https://github.com/dmauser/PrivateLink/tree/master/PLS-for-Onprem-workloads)
    - [LAB: Publish On-premises Workloads using Private Link Service + HAProxy](https://github.com/dmauser/Lab/tree/master/PLS-for-onprem-workloads-haproxy)
  - [Network Performance Considerations: Azure Files over Private Endpoint](https://github.com/dmauser/azure-files-netperf)

</details>

### Azure DNS

- [Azure DNS Private Resolver](https://github.com/dmauser/azure-dns-private-resolver) *(Last updated: Jan 2026)*
  - [LAB: Azure DNS Private Resolver — Hub and Spoke](https://github.com/dmauser/azure-dns-private-resolver/tree/main/adr-lab)
- [LAB: Azure DNS Security Policy](https://github.com/dmauser/AzDnsSecurityPolicyLab) *(Last updated: Mar 2026)*

### Azure Files

- [Network Performance Considerations when Using Azure Files over Private Endpoint](https://github.com/dmauser/azure-files-netperf) *(Last updated: Oct 2021)*

---

## Firewall & Network Security

- [LAB: Azure Firewall to Inspect Traffic between VPN and ExpressRoute](https://github.com/dmauser/Lab/tree/master/RS-ER-VPN-Gateway-Transit-AzFW)
- [LAB: Virtual WAN — Route Traffic Through Azure Firewall Spoke](https://github.com/dmauser/azure-virtualwan/tree/main/inter-region-azfw)
- [LAB: Secured Virtual Hubs and Routing Intent (Intra-Region)](https://github.com/dmauser/azure-virtualwan/tree/main/nva-spoke-internet)
- [LAB: Secured Virtual Hubs Inter-region via ExpressRoute](https://github.com/dmauser/azure-virtualwan/tree/main/svh-inter-region-er)

---

## Core Networking & Edge

### Azure Virtual Network

- [LAB: Azure Virtual Network Encryption](https://github.com/dmauser/azure-vnet-encryption) *(Last updated: Feb 2026)*

### Azure Front Door

- [LAB: Azure Front Door and Private Link Service](https://github.com/dmauser/azure-frontdoor-pls) *(Last updated: Sep 2025)*

### Azure VMware Solution (AVS)

- [LAB: AVS (ER) to On-prem (ER) Transit using Secured vHub + Routing Intent](https://github.com/dmauser/azure-vmware-solution) *(Last updated: Jun 2025)*

### Running DHCP Server on Azure

- [Running DHCP Server on Azure VM](https://github.com/dmauser/DHCPServer-On-Azure) *(Last updated: May 2024)*

### Random Scripts

- [Random Scripts @ GitHub Gist](https://gist.github.com/dmauser)

---

## GCP & Multi-Cloud

- [GCP Base Networking Lab](https://github.com/dmauser/gcp-network-base-lab) *(Last updated: Sep 2022)*
- [LAB: GCP Site-to-Site VPN with Azure](https://github.com/dmauser/azure-vpn-s2s-gcp) *(Last updated: Jan 2022)*

---

## Recommended Repos

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

## GitHub Statistics

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=dmauser&show_icons=true&theme=default" alt="dmauser's GitHub stats">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=dmauser&layout=compact&theme=default" alt="dmauser's top languages">
</p>
