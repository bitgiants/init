/*
# deploy eve-ng from local ova template
resource "vsphere_virtual_machine" "eve-ng" {
  name = "eve-ng"
  resource_pool_id = data.vsphere_resource_pool.pool.id
  datastore_id = data.vsphere_datastore.datastore.id
  datacenter_id = data.vsphere_datacenter.dc.id
  host_system_id = data.vsphere_host.host.id
  num_cpus = 2
  memory = 4096
  wait_for_guest_ip_timeout = 0
  wait_for_guest_net_timeout = 0

  ovf_deploy {
    local_ovf_path = data.vsphere_ovf_vm_template.ovfLocal.local_ovf_path
    ovf_network_map = data.vsphere_ovf_vm_template.ovfLocal.ovf_network_map
    disk_provisioning = "thin"
  }
}
*/

# deploy jenkins from remote ova template
resource "vsphere_virtual_machine" "jenkins" {
  name = "jenkins"
  resource_pool_id = data.vsphere_resource_pool.pool.id
  datastore_id = data.vsphere_datastore.datastore.id
  datacenter_id = data.vsphere_datacenter.dc.id
  host_system_id = data.vsphere_host.host.id
  num_cpus = 4
  memory = 8192
  wait_for_guest_ip_timeout = 0
  wait_for_guest_net_timeout = 0

  ovf_deploy {
    remote_ovf_url = data.vsphere_ovf_vm_template.ovaJenkinsRemote.remote_ovf_url
    ovf_network_map = data.vsphere_ovf_vm_template.ovaJenkinsRemote.ovf_network_map
    disk_provisioning = "thin"
  }
}

# deploy eve-ng from remote ova template
resource "vsphere_virtual_machine" "eve-ng" {
  name = "eve-ng"
  resource_pool_id = data.vsphere_resource_pool.pool.id
  datastore_id = data.vsphere_datastore.datastore.id
  datacenter_id = data.vsphere_datacenter.dc.id
  host_system_id = data.vsphere_host.host.id
  num_cpus = 4
  memory = 8192
  wait_for_guest_ip_timeout = 0
  wait_for_guest_net_timeout = 0

  ovf_deploy {
    remote_ovf_url = data.vsphere_ovf_vm_template.ovaEveRemote.remote_ovf_url
    ovf_network_map = data.vsphere_ovf_vm_template.ovaEveRemote.ovf_network_map
    disk_provisioning = "thin"
  }
}
