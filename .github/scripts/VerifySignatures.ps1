param (
    [Parameter(Mandatory = $true)][string]$arch
)

$files = $(Get-ChildItem -Path "out\installer\build\universalflashcards\windows\visualstudio\$arch\Release" -Recurse -Include *.exe, *.dll, *.pyd)
if (-not $files) {
    Write-Error "No binaries found for $arch"
}

$failed = 0
foreach ($file in $files) {
    $sig = Get-AuthenticodeSignature $file.FullName
    if ($sig.Status -ne "Valid") {
        Write-Host "::error::$($file.FullName) signature status: $($sig.Status)"
        $failed++
    }
}
if ($failed) {
    Write-Host "$failed of $($files.Count) binaries have no valid signature"
    exit 1
}

$universalflashcards = Get-AuthenticodeSignature "out\installer\build\universalflashcards\windows\visualstudio\$arch\Release\Universal Flashcards.exe"
Write-Host "All $($files.Count) binaries have a valid signature. Universal Flashcards.exe signer: $($universalflashcards.SignerCertificate.Subject)"
