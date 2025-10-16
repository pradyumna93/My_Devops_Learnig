Disable-AzContextAutosave

Connect-AzAccount
$Resource_GroupName = "myResourceGroup"
$location = "EastUS"
New-AzResourceGroup -Name $Resource_GroupName -Location $location


##########################
# Create Reource Group Through Service Principal
##########################

$APPId = "abcd-123-xyz"
$App_Secret = "xya23fjjjdsb4234b9h9h9"
$Tenant_Id = "72f988bf-86f1-41af-91ab-2d7cd011db47"
$SecureApp_Secret = $App_Secret | ConvertTo-SecureString -String $App_Secret -AsPlainText -Force
$Credential = New-Object -TypeName System.Management.Automation.PSCredential `
-ArgumentList $APPId, $SecureApp_Secret
Connect-AzAccount -ServicePrincipal -Credential $Credential -Tenant $Tenant_Id

ResourceGroup = New-AzResourceGroup -Name $Resource_GroupName -Location $location

#print provisioning state of resource group
'Provisioning State' + $ResourceGroup.ProvisioningState

# Get Resource Group
$ResourceGroupExist = Get-AzResourceGroup -Name $Resource_GroupName
$ResourceGroupExist

# Get All Resource Groups
Get-AzResourceGroup
##########################
# --- Remove Resource Group ---
Remove-AzResourceGroup -Name $Resource_GroupName -Force
# --- IGNORE ---

# --- Remove All Resource Group ---

# Get-AzResourceGroup | ForEach-Object { Remove-AzResourceGroup -Name $_.ResourceGroupName -Force }

$ALLResourceGroups = Get-AzResourceGroup
foreach ($ResourceGroup in $ALLResourceGroups) {
    'Removing Resource Group: ' + $ResourceGroup.ResourceGroupName
    Remove-AzResourceGroup -Name $ResourceGroup.ResourceGroupName -Force
}