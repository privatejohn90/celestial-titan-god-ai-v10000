#!/bin/bash
echo "💠 Titan Auto-Restore System v10 000.7-AHR"
cd ~/Desktop/titan_dual_state_lab

VAULT="data/titan_v10000_7_FXR.vault"
TARGETS=("titan_memory.json" "titan_results.json" "titan_forecasts.json" "titan_accuracy.json" "titan_theme.json" "titan_cloud_vault.json")

if [ ! -f "$VAULT" ]; then
    echo "⚠️  Vault file missing: $VAULT"
    echo "❌  Cannot restore — please re-sync from Titan Cloud or GitHub."
    exit 1
fi

echo "🔍 Checking essential Titan core files..."
for file in "${TARGETS[@]}"; do
    if [ ! -f "$file" ]; then
        echo "🧩 Missing: $file → restoring from vault..."
        cp "$VAULT" "data/$file"
        echo "✅ Restored $file"
    else
        echo "🟢 OK: $file"
    fi
done

echo "✨ All missing components restored. Titan Core stable again."
