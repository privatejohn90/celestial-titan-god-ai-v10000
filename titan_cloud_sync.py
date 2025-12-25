# ==========================================================
# ☁️ Titan Cloud Sync Engine v10,002
# ==========================================================
import os, time, subprocess, threading

def titan_cloud_sync():
    """Manual Cloud Sync to GitHub"""
    print("🚀 Starting Titan Cloud Sync...")
    try:
        # Commit & Push
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Titan AutoSync – Manual Cloud Sync"], check=False)
        subprocess.run(["git", "push"], check=True)
        print("✅ Titan Cloud Sync completed successfully!")
    except Exception as e:
        print("❌ Titan Cloud Sync failed:", e)

def titan_auto_background_sync(interval=300):
    """Automatic background Git sync every X seconds"""
    def auto_sync_loop():
        while True:
            try:
                print("🌐 Titan Auto Background Sync triggered...")
                subprocess.run(["git", "add", "."], check=True)
                subprocess.run(["git", "commit", "-m", "Titan AutoSync – Background Update"], check=False)
                subprocess.run(["git", "push"], check=True)
                print("✅ Titan Auto Background Sync done.")
            except Exception as e:
                print("❌ Titan Auto Background Sync failed:", e)
            time.sleep(interval)

    threading.Thread(target=auto_sync_loop, daemon=True).start()
    print(f"🌐 Titan Auto Background Sync Engine started (every {interval/60:.1f} min)")
