#!/usr/bin/env pwsh
# voz installer (Windows / PowerShell).
# Installs the voz skill into ~/.claude/skills/voz, which both the Claude Code CLI
# and the VSCode extension read.
#
#   ./install.ps1              install the skill only (invoke it when you want it)
#   ./install.ps1 -AlwaysOn    also wire the global CLAUDE.md pointer + SessionStart
#                              hook so the default voice applies every session
#
# Idempotent: safe to re-run. The -AlwaysOn wiring needs Python on your PATH.

[CmdletBinding()]
param([switch]$AlwaysOn)

$ErrorActionPreference = 'Stop'
$Repo = 'https://github.com/ojesusmp/voz.git'

$claude = Join-Path $HOME '.claude'
$dest = Join-Path $claude 'skills\voz'

# Resolve the source: the repo this script sits in, or a fresh shallow clone.
$scriptDir = if ($PSCommandPath) { Split-Path -Parent $PSCommandPath } else { $null }
$cloned = $null
if ($scriptDir -and (Test-Path (Join-Path $scriptDir 'SKILL.md'))) {
    $src = $scriptDir
} else {
    $cloned = Join-Path ([IO.Path]::GetTempPath()) ('voz-' + [Guid]::NewGuid().ToString('N'))
    Write-Host "Cloning voz from $Repo ..."
    git clone --depth 1 $Repo $cloned 2>&1 | Out-Null
    if (-not (Test-Path (Join-Path $cloned 'SKILL.md'))) {
        throw "Clone failed: SKILL.md not found in $cloned"
    }
    $src = $cloned
}

# Copy the skill files.
New-Item -ItemType Directory -Force -Path $dest, (Join-Path $dest 'references'), (Join-Path $dest 'scripts') | Out-Null
Copy-Item (Join-Path $src 'SKILL.md'), (Join-Path $src 'README.md'), (Join-Path $src 'LICENSE') $dest -Force
Copy-Item (Join-Path $src 'references\*') (Join-Path $dest 'references') -Force
Copy-Item (Join-Path $src 'scripts\*') (Join-Path $dest 'scripts') -Force
Write-Host "voz skill installed to $dest" -ForegroundColor Green

# Optional always-on wiring.
if ($AlwaysOn) {
    $py = Get-Command python -ErrorAction SilentlyContinue
    if (-not $py) { $py = Get-Command python3 -ErrorAction SilentlyContinue }
    if (-not $py) {
        Write-Warning 'python not found on PATH; skipping always-on wiring. Install Python, then re-run with -AlwaysOn.'
    } else {
        & $py.Source (Join-Path $dest 'scripts\wire_settings.py') --python $py.Name
    }
}

if ($cloned) { Remove-Item -Recurse -Force $cloned -ErrorAction SilentlyContinue }
Write-Host 'Done. Reload VSCode (Developer: Reload Window) or start a new Claude Code session.' -ForegroundColor Cyan
