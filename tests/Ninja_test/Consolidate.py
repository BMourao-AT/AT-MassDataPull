import Auth
import Devices
import Orgs

def consolidate(orgData, deviceData):
    customerSummary = []
    orgData = sorted(orgData, key=lambda x: x["name"])
    for org in orgData:
        customerSummary.append({
            "OrgName": org["name"],
            "OrgID": org["id"],
            "DeviceCount": 0
        })
    for device in deviceData:
        deviceOrg = device.get("organizationId")
        for customer in customerSummary:
            if deviceOrg == customer["OrgID"]:
                customer["DeviceCount"] += 1
                break
    return customerSummary

if __name__ == "__main__":
    authData = Auth.get_auth()
    orgData = Orgs.get_orgs(authData["authToken"])
    deviceData = Devices.get_devices(authData["authToken"])
    
    customerSummary = consolidate(orgData, deviceData)
    for num, org in enumerate(customerSummary, start=1):
        print(f'Organization number {num}: {org["OrgName"]} | Device count: {org["DeviceCount"]}')
    