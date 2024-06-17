#!/usr/bin/env python3

def main():
    print("Welcome to the Clab help Options Selector!")
    print("1. deploy_commands")
    print("2. Connecting_to_the_nodes")
    print("3. destroy_commands")
    print("4. inspect_commands")
    print("5. save_commands")
    print("6. graph_commands")
    print("7. Exit")

    while True:
        choice = input("Please enter your choice: ")

        if choice == '1':
            deploy_commands()
        elif choice == '2':
            Connecting_to_the_nodes()     
        elif choice == '3':
            destroy_commands()
        elif choice == '4':
            inspect_commands()
        elif choice == '5':
            save_commands()
        elif choice == '6':
            graph_commands()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


def deploy_commands():
    print("\n #Deploy a lab using the given topology file\n\n containerlab deploy -t <lab name>\n\n #Deploy a lab and regenerate all configuration artifacts\n\n containerlab deploy -t <lab name> --reconfigure\n")

def Connecting_to_the_nodes():
    print("\n #Connecting to the nodes\n\n docker exec -it <node name> sr_cli\n\n docker exec -it <name> bash\n\n ssh admin@<node mgmt ip>\n\n ( for SRL node use sr_cli and for XRd use /pkg/bin/xr_cli.sh )\n")

def destroy_commands():
    print("\n #Destroy a lab described in the given topology file\n\n containerlab destroy -t <lab name>\n\n #Destroy a lab and remove the Lab directory\n\n containerlab destroy -t <lab name> --cleanup\n\n #Destroy all labs on the container host\n\n containerlab destroy -a\n")


def inspect_commands():
    print("\n #List all running labs on the host\n\n containerlab inspect --all\n\n #Provide information about a specific running lab by its name\n\n containerlab inspect --name <lab name>\n")


def save_commands():
    print("\n #Save the configuration of the containers in a specific lab\n\n containerlab save -n <lab name>\n")


def graph_commands():
    print("\n #generates a graphical representations of a topology and access the topology in browser using VM IP and given Port No.\n\n containerlab graph -t <path/to/topo.clab.yml>\n\n #Render graph on specified http server port\n\n containerlab graph --topo /path/to/topo1.clab.yml --srv :3002\n")

if __name__ == "__main__":
    main()
