data "vsphere_datacenter" "dc" {
  name = var.vsphere_datacenter
}

data "vsphere_datastore" "datastore" {
  name          = "datastore1"
  datacenter_id = data.vsphere_datacenter.dc.id
}

data "vsphere_network" "network" {
  name = "VM Network"
  datacenter_id = data.vsphere_datacenter.dc.id
}

data "vsphere_resource_pool" "pool" {
  name          = "10.200.10.53/Resources"
  datacenter_id = data.vsphere_datacenter.dc.id
}

data "vsphere_host" "host" {
  name          = var.vsphere_host_name
  datacenter_id = data.vsphere_datacenter.dc.id
}

## Remote OVA Source
data "vsphere_ovf_vm_template" "ovaJenkinsRemote" {
  name              = "jenkins"
  disk_provisioning = "thin"
  resource_pool_id  = data.vsphere_resource_pool.pool.id
  datastore_id      = data.vsphere_datastore.datastore.id
  host_system_id    = data.vsphere_host.host.id
  remote_ovf_url    = "https://bg-automation.s3.eu-central-1.amazonaws.com/jenkins.ova"
  ovf_network_map   = {
    "VM Network" : data.vsphere_network.network.id
  }
}

data "vsphere_ovf_vm_template" "ovaEveRemote" {
  name              = "eve-ng"
  disk_provisioning = "thin"
  resource_pool_id  = data.vsphere_resource_pool.pool.id
  datastore_id      = data.vsphere_datastore.datastore.id
  host_system_id    = data.vsphere_host.host.id
  remote_ovf_url    = "https://bg-automation.s3.eu-central-1.amazonaws.com/automation-eve-lab-v3.ova"
  ovf_network_map   = {
    "VM Network" : data.vsphere_network.network.id
  }
}
/*
## Local OVA Source
data "vsphere_ovf_vm_template" "ovfLocal" {
  name              = "eve-ng"
  disk_provisioning = "thin"
  resource_pool_id  = data.vsphere_resource_pool.pool.id
  datastore_id      = data.vsphere_datastore.datastore.id
  host_system_id    = data.vsphere_host.host.id
  local_ovf_path    = "/Users/oleksii/Downloads/out/automation-eve-lab-v3.ova"
  ovf_network_map   = {
    "VM Network" : data.vsphere_network.network.id
  }
}
*/
