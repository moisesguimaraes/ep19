source vaultrc

vault operator unseal $VAULT_UK3 && vault operator unseal $VAULT_UK2 && vault operator unseal $VAULT_UK1

echo $VAULT_TOKEN | pbcopy
echo "\n!!! Vault ROOT TOKEN copied to clipboard !!!"