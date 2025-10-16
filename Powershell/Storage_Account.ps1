
$StorageAccountName = "mystorageaccountpradyu"
$Resource_GroupName = "myResourceGroup"
$location = "EastUS"
$SkuName = "Standard_LRS"
$Kind = "StorageV2" 


# Create Storage Account
$StorageAccount = New-AzStorageAccount -ResourceGroupName $Resource_GroupName `
    -Name $StorageAccountName `
    -Location $location `
    -SkuName $SkuName `
    -Kind $Kind
$StorageAccount

# Get Storage Account
$StorageAccountExist = Get-AzStorageAccount -ResourceGroupName $Resource_GroupName `
    -Name $StorageAccountName
$StorageAccountExist

# Get All Storage Accounts
Get-AzStorageAccount    

# Remove Storage Account
Remove-AzStorageAccount -ResourceGroupName $Resource_GroupName `
    -Name $StorageAccountName -Force
# --- IGNORE ---
# Remove All Storage Accounts
# Get-AzStorageAccount | ForEach-Object { Remove-AzStorageAccount -ResourceGroupName $_.ResourceGroupName -Name $_.StorageAccountName -Force }
$ALLStorageAccounts = Get-AzStorageAccount
foreach ($StorageAccount in $ALLStorageAccounts) {
    'Removing Storage Account: ' + $StorageAccount.StorageAccountName
    Remove-AzStorageAccount -ResourceGroupName $StorageAccount.ResourceGroupName -Name $StorageAccount.StorageAccountName -Force
}

# --- IGNORE ---

# Create a container in the storage account
$ctx = $StorageAccount.Context
New-AzStorageContainer -Name "mycontainer" -Context $ctx

# List all containers in the storage account
Get-AzStorageContainer -Context $ctx    

# Upload a file to the container
$localFilePath = "C:\path\to\your\file.txt"
Set-AzStorageBlobContent -File $localFilePath -Container "mycontainer" -Context $ctx    

# Download a file from the container
$blobName = "file.txt"
$destinationPath = "C:\path\to\download\file.txt"
Get-AzStorageBlobContent -Container "mycontainer" -Blob $blobName -Destination $destinationPath `
-Context $ctx   
# Delete a blob from the container
Remove-AzStorageBlob -Container "mycontainer" -Blob $blobName -Context $ctx -Force
# Delete the container
Remove-AzStorageContainer -Name "mycontainer" -Context $ctx -Force
# --- IGNORE ---    

