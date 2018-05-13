import time
import botbook_mcp3002 as mcp
import dweepy

def main():
    while True:
        smokeLevel = mcp.readAnalog(0,0)
        print("Current smoke level is %i " % smokeLevel)
        if smokeLevel > 120:
            print("Smoke detected")
            dweepy.dweet_for('sensorgas_viro', {'Estat':'Gas detectat'})
        time.sleep(5)

if __name__ == "__main__":
main()

