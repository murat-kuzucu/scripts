#PowerShell Port Scanner

param (
    [string[]]$TargetHosts = @("127.0.0.1"),  # Default to localhost
    [string[]]$Ports = @("1-1024")           # Default port range
)

function Test-Port {
    param (
        [string]$IP,
        [int]$Port
    )

    try {
        # Attempt to connect to the port
        $Connection = New-Object System.Net.Sockets.TcpClient
        $Connection.Connect($IP, $Port)
        $Connection.Close()
        return $true
    } catch {
        return $false
    }
}

function Parse-Ports {
    param (
        [string[]]$PortInput
    )

    $PortList = @()
    foreach ($Port in $PortInput) {
        if ($Port -match "^(\d+)-(\d+)$") {
            # If port range is specified, expand it
            $StartPort = [int]$Matches[1]
            $EndPort = [int]$Matches[2]
            $PortList += $StartPort..$EndPort
        } elseif ($Port -match "^\d+$") {
            # If single port is specified, add it
            $PortList += [int]$Port
        }
    }
    return $PortList | Sort-Object -Unique
}

# Parse the ports input
$ParsedPorts = Parse-Ports -PortInput $Ports

foreach ($Host in $TargetHosts) {
    Write-Host "Scanning $Host for ports: $($ParsedPorts -join ", ")" -ForegroundColor Cyan

    foreach ($Port in $ParsedPorts) {
        if (Test-Port -IP $Host -Port $Port) {
            Write-Host "[+] $Host:$Port is OPEN" -ForegroundColor Green
        } else {
            Write-Host "[-] $Host:$Port is CLOSED" -ForegroundColor Red
        }
    }
}

Write-Host "Scan complete!" -ForegroundColor Cyan
