# redborder-selinux

This repository contains the **SELinux policies** required for the **redborder** platform.
The `.te` files defined here adjust and extend SELinux security rules so that redborder services and components can operate properly in environments with SELinux enabled.

---

## Checking for Required Policies

If some redborder services are being blocked by SELinux, you can analyze the denial logs and generate a module with the missing rules using:

```cmd
audit2allow -a -M latest_policies
```

This command:

- Reads all recent SELinux denials from the audit log.
- Generates a new SELinux policy module (`latest_policies.pp`).

#### Platforms

- Rocky Linux 9

## 🔧 Usage

1. Modify the policies
2. Create the rpm with `sudo make rpm`
3. Upload to your manager and install it
4. Run `chef-client` and will apply the policies

## Contributing

1. Fork the repository on Github
2. Create a named feature branch (like add_component_x)
3. Write your change
4. Write tests for your change (if applicable)
5. Run the tests, ensuring they all pass
6. Submit a Pull Request using Github

## License and Authors

- David Vanhoucke <dvanhoucke@redborder.com>
- Miguel Negrón <manegron@redborder.com>
- Miguel Álvarez <malvarez@redborder.com>
- Nils Verschaeve <nverschaeve@redborder.com>
- Luis Blanco <ljblanco@redborder.com>
- Julio Peralta <jperalta@redborder.com>
- Juan Soto <jsoto@redborder.com>
- Rafael Gómez <rgomez@redborder.com>
- Pablo Pérez González <pperez@redborder.com>
