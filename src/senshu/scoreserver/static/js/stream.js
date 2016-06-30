var stream_message =  ''+
'[    0.000000] Initializing cgroup subsys cpuset\n'+
'[    0.000000] Initializing cgroup subsys cpu\n'+
'[    0.000000] Initializing cgroup subsys cpuacct\n'+
'[    0.000000] KERNEL supported cpus:\n'+
'[    0.000000]   Intel GenuineIntel\n'+
'[    0.000000]   AMD AuthenticAMD\n'+
'[    0.000000]   Centaur CentaurHauls\n'+
'[    0.000000] e820: BIOS-provided physical RAM map:\n'+
'[    0.000000] BIOS-e820: [mem 0x0000000000000000-0x000000000009fbff] usable\n'+
'[    0.000000] BIOS-e820: [mem 0x000000000009fc00-0x000000000009ffff] reserved\n'+
'[    0.000000] BIOS-e820: [mem 0x00000000000f0000-0x00000000000fffff] reserved\n'+
'[    0.000000] BIOS-e820: [mem 0x0000000000100000-0x000000001ffeffff] usable\n'+
'[    0.000000] BIOS-e820: [mem 0x000000001fff0000-0x000000001fffffff] ACPI data\n'+
'[    0.000000] BIOS-e820: [mem 0x00000000fffc0000-0x00000000ffffffff] reserved\n'+
'[    0.000000] NX (Execute Disable) protection: active\n'+
'[    0.000000] SMBIOS 2.5 present.\n'+
'[    0.000000] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved\n'+
'[    0.000000] e820: remove [mem 0x000a0000-0x000fffff] usable\n'+
'[    0.000000] No AGP bridge found\n'+
'[    0.000000] e820: last_pfn = 0x1fff0 max_arch_pfn = 0x400000000\n'+
'[    0.000000] MTRR default type: uncachable\n'+
'[    0.000000] MTRR variable ranges disabled:\n'+
'[    0.000000] x86 PAT enabled: cpu 0, old 0x7040600070406, new 0x7010600070106\n'+
'[    0.000000] CPU MTRRs all blank - virtualized system.\n'+
'[    0.000000] found SMP MP-table at [mem 0x0009fff0-0x0009ffff] mapped at [ffff88000009fff0]\n'+
'[    0.000000] Scanning 1 areas for low memory corruption\n'+
'[    0.000000] Base memory trampoline at [ffff880000099000] 99000 size 24576\n'+
'[    0.000000] init_memory_mapping: [mem 0x00000000-0x000fffff]\n'+
'[    0.000000]  [mem 0x00000000-0x000fffff] page 4k\n'+
'[    0.000000] BRK [0x01fe2000, 0x01fe2fff] PGTABLE\n'+
'[    0.000000] BRK [0x01fe3000, 0x01fe3fff] PGTABLE\n'+
'[    0.000000] BRK [0x01fe4000, 0x01fe4fff] PGTABLE\n'+
'[    0.000000] init_memory_mapping: [mem 0x1fc00000-0x1fdfffff]\n'+
'[    0.000000]  [mem 0x1fc00000-0x1fdfffff] page 2M\n'+
'[    0.000000] init_memory_mapping: [mem 0x1c000000-0x1fbfffff]\n'+
'[    0.000000]  [mem 0x1c000000-0x1fbfffff] page 2M\n'+
'[    0.000000] init_memory_mapping: [mem 0x00100000-0x1bffffff]\n'+
'[    0.000000]  [mem 0x00100000-0x001fffff] page 4k\n'+
'[    0.000000]  [mem 0x00200000-0x1bffffff] page 2M\n'+
'[    0.000000] init_memory_mapping: [mem 0x1fe00000-0x1ffeffff]\n'+
'[    0.000000]  [mem 0x1fe00000-0x1ffeffff] page 4k\n'+
'[    0.000000] BRK [0x01fe5000, 0x01fe5fff] PGTABLE\n'+
'[    0.000000] RAMDISK: [mem 0x1f179000-0x1f86bfff]\n'+
'[    0.000000] ACPI: RSDP 00000000000e0000 000024 (v02 VBOX  )\n'+
'[    0.000000] ACPI: XSDT 000000001fff0030 00003C (v01 VBOX   VBOXXSDT 00000001 ASL  00000061)\n'+
'[    0.000000] ACPI: FACP 000000001fff00f0 0000F4 (v04 VBOX   VBOXFACP 00000001 ASL  00000061)\n'+
'[    0.000000] ACPI: DSDT 000000001fff0470 001B96 (v01 VBOX   VBOXBIOS 00000002 INTL 20100528)\n'+
'[    0.000000] ACPI: FACS 000000001fff0200 000040\n'+
'[    0.000000] ACPI: APIC 000000001fff0240 000054 (v02 VBOX   VBOXAPIC 00000001 ASL  00000061)\n'+
'[    0.000000] ACPI: SSDT 000000001fff02a0 0001CC (v01 VBOX   VBOXCPUT 00000002 INTL 20100528)\n'+
'[    0.000000] ACPI: Local APIC address 0xfee00000\n'+
'[    0.000000] No NUMA configuration found\n'+
'[    0.000000] Faking a node at [mem 0x0000000000000000-0x000000001ffeffff]\n'+
'[    0.000000] Initmem setup node 0 [mem 0x00000000-0x1ffeffff]\n'+
'[    0.000000]   NODE_DATA [mem 0x1ffeb000-0x1ffeffff]\n'+
'[    0.000000]  [ffffea0000000000-ffffea00007fffff] PMD -> [ffff88001e400000-ffff88001ebfffff] on node 0\n'+
'[    0.000000] Zone ranges:\n'+
'[    0.000000]   DMA      [mem 0x00001000-0x00ffffff]\n'+
'[    0.000000]   DMA32    [mem 0x01000000-0xffffffff]\n'+
'[    0.000000]   Normal   empty\n'+
'[    0.000000] Movable zone start for each node\n'+
'[    0.000000] Early memory node ranges\n'+
'[    0.000000]   node   0: [mem 0x00001000-0x0009efff]\n'+
'[    0.000000]   node   0: [mem 0x00100000-0x1ffeffff]\n'+
'[    0.000000] On node 0 totalpages: 130958\n'+
'[    0.000000]   DMA zone: 64 pages used for memmap\n'+
'[    0.000000]   DMA zone: 21 pages reserved\n'+
'[    0.000000]   DMA zone: 3998 pages, LIFO batch:0\n'+
'[    0.000000]   DMA32 zone: 1984 pages used for memmap\n'+
'[    0.000000]   DMA32 zone: 126960 pages, LIFO batch:31\n'+
'[    0.000000] ACPI: PM-Timer IO Port: 0x4008\n'+
'[    0.000000] ACPI: Local APIC address 0xfee00000\n'+
'[    0.000000] ACPI: LAPIC (acpi_id[0x00] lapic_id[0x00] enabled)\n'+
'[    0.000000] ACPI: IOAPIC (id[0x01] address[0xfec00000] gsi_base[0])\n'+
'[    0.000000] IOAPIC[0]: apic_id 1, version 17, address 0xfec00000, GSI 0-23\n'+
'[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 dfl dfl)\n'+
'[    0.000000] ACPI: INT_SRC_OVR (bus 0 bus_irq 9 global_irq 9 high level)\n'+
'[    0.000000] ACPI: IRQ0 used by override.\n'+
'[    0.000000] ACPI: IRQ2 used by override.\n'+
'[    0.000000] ACPI: IRQ9 used by override.\n'+
'[    0.000000] Using ACPI (MADT) for SMP configuration information\n'+
'[    0.000000] smpboot: Allowing 1 CPUs, 0 hotplug CPUs\n'+
'[    0.000000] nr_irqs_gsi: 40\n'+
'[    0.000000] PM: Registered nosave memory: [mem 0x0009f000-0x0009ffff]\n'+
'[    0.000000] PM: Registered nosave memory: [mem 0x000a0000-0x000effff]\n'+
'[    0.000000] PM: Registered nosave memory: [mem 0x000f0000-0x000fffff]\n'+
'[    0.000000] e820: [mem 0x20000000-0xfffbffff] available for PCI devices\n'+
'[    0.000000] Booting paravirtualized kernel on bare hardware\n'+
'[    0.000000] setup_percpu: NR_CPUS:256 nr_cpumask_bits:256 nr_cpu_ids:1 nr_node_ids:1\n'+
'[    0.000000] PERCPU: Embedded 27 pages/cpu @ffff88001fc00000 s81536 r8192 d20864 u2097152\n'+
'[    0.000000] pcpu-alloc: s81536 r8192 d20864 u2097152 alloc=1*2097152\n'+
'[    0.000000] pcpu-alloc: [0] 0\n'+
'[    0.000000] Built 1 zonelists in Node order, mobility grouping on.  Total pages: 128889\n'+
'[    0.000000] Policy zone: DMA32\n'+
'[    0.000000] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-3.13.0-87-generic root=UUID=1594814a-7a6c-4bc3-8135-055785b4c90c ro console=tty1 console=ttyS0\n'+
'[    0.000000] PID hash table entries: 2048 (order: 2, 16384 bytes)\n'+
'[    0.000000] Checking aperture...\n'+
'[    0.000000] No AGP bridge found\n'+
'[    0.000000] Calgary: detecting Calgary via BIOS EBDA area\n'+
'[    0.000000] Calgary: Unable to locate Rio Grande table in EBDA - bailing!\n'+
'[    0.000000] Memory: 491788K/523832K available (7418K kernel code, 1146K rwdata, 3416K rodata, 1336K init, 1448K bss, 32044K reserved)\n'+
'[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=1, Nodes=1\n'+
'[    0.000000] Hierarchical RCU implementation.\n'+
'[    0.000000] 	RCU dyntick-idle grace-period acceleration is enabled.\n'+
'[    0.000000] 	RCU restricting CPUs from NR_CPUS=256 to nr_cpu_ids=1.\n'+
'[    0.000000] 	Offload RCU callbacks from all CPUs\n'+
'[    0.000000] 	Offload RCU callbacks from CPUs: 0.\n'+
'[    0.000000] NR_IRQS:16640 nr_irqs:256 16\n'+
'[    0.000000] Console: colour VGA+ 80x25\n'+
'[    0.000000] console [tty1] enabled\n'+
'[    0.000000] console [ttyS0] enabled\n'+
'[    0.000000] allocated 2097152 bytes of page_cgroup\n'+
'[    0.000000] please try "cgroup_disable=memory" option if you don"t want memory cgroups\n'+
'[    0.000000] tsc: Fast TSC calibration failed\n'+
'[    0.000000] tsc: Unable to calibrate against PIT\n'+
'[    0.000000] tsc: using PMTIMER reference calibration\n'+
'[    0.000000] tsc: Detected 2293.566 MHz processor\n'+
'[    0.016003] Calibrating delay loop (skipped), value calculated using timer frequency.. 4587.13 BogoMIPS (lpj=9174264)\n'+
'[    0.017338] pid_max: default: 32768 minimum: 301\n'+
'[    0.020037] Security Framework initialized\n'+
'[    0.020674] AppArmor: AppArmor initialized\n'+
'[    0.021363] Yama: becoming mindful.\n'+
'[    0.022006] Dentry cache hash table entries: 65536 (order: 7, 524288 bytes)\n'+
'[    0.022964] Inode-cache hash table entries: 32768 (order: 6, 262144 bytes)\n'+
'[    0.024065] Mount-cache hash table entries: 1024 (order: 1, 8192 bytes)\n'+
'[    0.025172] Mountpoint-cache hash table entries: 1024 (order: 1, 8192 bytes)\n'+
'[    0.026212] Initializing cgroup subsys memory\n'+
'[    0.026861] Initializing cgroup subsys devices\n'+
'[    0.027508] Initializing cgroup subsys freezer\n'+
'[    0.028000] Initializing cgroup subsys blkio\n'+
'[    0.028612] Initializing cgroup subsys perf_event\n'+
'[    0.029371] Initializing cgroup subsys hugetlb\n'+
'[    0.030244] mce: CPU supports 0 MCE banks\n'+
'[    0.032249] process: using mwait in idle threads\n'+
'[    0.032997] Last level iTLB entries: 4KB 512, 2MB 0, 4MB 0\n'+
'[    0.032997] Last level dTLB entries: 4KB 512, 2MB 32, 4MB 32\n'+
'[    0.032997] tlb_flushall_shift: 2\n'+
'[    0.067021] Freeing SMP alternatives memory: 32K (ffffffff81e6e000 - ffffffff81e76000)\n'+
'[    0.078747] ACPI: Core revision 20131115\n'+
'[    0.080000] ACPI: All ACPI Tables successfully acquired\n'+
'[    0.080831] ftrace: allocating 28609 entries in 112 pages\n'+
'[    0.096890] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1\n'+
'[    0.148000] smpboot: CPU0: Intel(R) Core(TM) i5-3427U CPU @ 1.80GHz (fam: 06, model: 3a, stepping: 09)\n'+
'[    0.152000] Performance Events: unsupported p6 CPU model 58 no PMU driver, software events only.\n'+
'[    0.152000] x86: Booted up 1 node, 1 CPUs\n'+
'[    0.152000] smpboot: Total of 1 processors activated (4587.13 BogoMIPS)\n'+
'[    0.152016] NMI watchdog: disabled (cpu0): hardware events not enabled\n'+
'[    0.154429] devtmpfs: initialized\n'+
'[    0.158116] EVM: security.selinux\n'+
'[    0.158689] EVM: security.SMACK64\n'+
'[    0.159477] EVM: security.ima\n'+
'[    0.160000] EVM: security.capability\n'+
'[    0.164736] pinctrl core: initialized pinctrl subsystem\n'+
'[    0.165600] regulator-dummy: no parameters\n'+
'[    0.166265] RTC time:  8:14:56, date: 06/28/16\n'+
'[    0.166943] NET: Registered protocol family 16\n'+
'[    0.167690] cpuidle: using governor ladder\n'+
'[    0.168004] cpuidle: using governor menu\n'+
'[    0.168646] ACPI: bus type PCI registered\n'+
'[    0.169415] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5\n'+
'[    0.170791] PCI: Using configuration type 1 for base access\n'+
'[    0.172801] bio: create slab <bio-0> at 0\n'+
'[    0.173639] ACPI: Added _OSI(Module Device)\n'+
'[    0.174678] ACPI: Added _OSI(Processor Device)\n'+
'[    0.175323] ACPI: Added _OSI(3.0 _SCP Extensions)\n'+
'[    0.175986] ACPI: Added _OSI(Processor Aggregator Device)\n'+
'[    0.177103] ACPI: Executed 1 blocks of module-level executable AML code\n'+
'[    0.181226] ACPI: Interpreter enabled\n'+
'[    0.181825] ACPI Exception: AE_NOT_FOUND, While evaluating Sleep State [\_S1_] (20131115/hwxface-580)\n'+
'[    0.183265] ACPI Exception: AE_NOT_FOUND, While evaluating Sleep State [\_S2_] (20131115/hwxface-580)\n'+
'[    0.183649] ACPI Exception: AE_NOT_FOUND, While evaluating Sleep State [\_S3_] (20131115/hwxface-580)\n'+
'[    0.185479] ACPI Exception: AE_NOT_FOUND, While evaluating Sleep State [\_S4_] (20131115/hwxface-580)\n'+
'[    0.187174] ACPI: (supports S0 S5)\n'+
'[    0.188171] ACPI: Using IOAPIC for interrupt routing\n'+
'[    0.189386] PCI: Ignoring host bridge windows from ACPI; if necessary, use "pci=use_crs" and report a bug\n'+
'[    0.190847] ACPI: No dock devices found.\n'+
'[    0.197863] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-ff])\n'+
'[    0.199257] acpi PNP0A03:00: _OSC: OS supports [ASPM ClockPM Segments MSI]\n'+
'[    0.200010] acpi PNP0A03:00: _OSC failed (AE_NOT_FOUND); disabling ASPM\n'+
'[    0.200922] acpi PNP0A03:00: host bridge window [io  0x0000-0x0cf7] (ignored)\n'+
'[    0.200925] acpi PNP0A03:00: host bridge window [io  0x0d00-0xffff] (ignored)\n'+
'[    0.200926] acpi PNP0A03:00: host bridge window [mem 0x000a0000-0x000bffff] (ignored)\n'+
'[    0.200928] acpi PNP0A03:00: host bridge window [mem 0x20000000-0xffdfffff] (ignored)\n'+
'[    0.200930] PCI: root bus 00: using default resources\n'+
'[    0.200941] acpi PNP0A03:00: fail to add MMCONFIG information, can"t access extended PCI configuration space under this bridge.\n'+
'[    0.202721] PCI host bridge to bus 0000:00\n'+
'[    0.204050] pci_bus 0000:00: root bus resource [bus 00-ff]\n'+
'[    0.205055] pci_bus 0000:00: root bus resource [io  0x0000-0xffff]\n'+
'[    0.205869] pci_bus 0000:00: root bus resource [mem 0x00000000-0xfffffffff]\n'+
'[    0.206718] pci 0000:00:00.0: [8086:1237] type 00 class 0x060000\n'+
'[    0.208388] pci 0000:00:01.0: [8086:7000] type 00 class 0x060100\n'+
'[    0.209285] pci 0000:00:02.0: [80ee:beef] type 00 class 0x030000\n'+
'[    0.210088] pci 0000:00:02.0: reg 0x10: [mem 0xe0000000-0xe0ffffff pref]\n'+
'[    0.214940] pci 0000:00:03.0: [8086:100e] type 00 class 0x020000\n'+
'[    0.215552] pci 0000:00:03.0: reg 0x10: [mem 0xf0000000-0xf001ffff]\n'+
'[    0.216470] pci 0000:00:03.0: reg 0x18: [io  0xd000-0xd007]\n'+
'[    0.218966] pci 0000:00:04.0: [80ee:cafe] type 00 class 0x088000\n'+
'[    0.219641] pci 0000:00:04.0: reg 0x10: [io  0xd020-0xd03f]\n'+
'[    0.220167] pci 0000:00:04.0: reg 0x14: [mem 0xf0400000-0xf07fffff]\n'+
'[    0.220785] pci 0000:00:04.0: reg 0x18: [mem 0xf0800000-0xf0803fff pref]\n'+
'[    0.223717] pci 0000:00:07.0: [8086:7113] type 00 class 0x068000\n'+
'[    0.225848] pci 0000:00:08.0: [8086:100e] type 00 class 0x020000\n'+
'[    0.226743] pci 0000:00:08.0: reg 0x10: [mem 0xf0820000-0xf083ffff]\n'+
'[    0.229036] pci 0000:00:08.0: reg 0x18: [io  0xd040-0xd047]\n'+
'[    0.232891] pci 0000:00:0d.0: [8086:2829] type 00 class 0x010601\n'+
'[    0.233467] pci 0000:00:0d.0: reg 0x10: [io  0xd048-0xd04f]\n'+
'[    0.234339] pci 0000:00:0d.0: reg 0x18: [io  0xd058-0xd05f]\n'+
'[    0.235050] pci 0000:00:0d.0: reg 0x20: [io  0xd070-0xd07f]\n'+
'[    0.235576] pci 0000:00:0d.0: reg 0x24: [mem 0xf0840000-0xf0841fff]\n'+
'[    0.238268] ACPI: PCI Interrupt Link [LNKA] (IRQs 5 9 10 *11)\n'+
'[    0.239915] ACPI: PCI Interrupt Link [LNKB] (IRQs 5 9 10 *11)\n'+
'[    0.240349] ACPI: PCI Interrupt Link [LNKC] (IRQs 5 9 *10 11)\n'+
'[    0.241725] ACPI: PCI Interrupt Link [LNKD] (IRQs 5 *9 10 11)\n'+
'[    0.243097] ACPI: Enabled 1 GPEs in block 00 to 07\n'+
'[    0.243951] ACPI: \_SB_.PCI0: notify handler is installed\n'+
'[    0.243962] Found 1 acpi root devices\n'+
'[    0.244000] vgaarb: setting as boot device: PCI:0000:00:02.0\n'+
'[    0.244000] vgaarb: device added: PCI:0000:00:02.0,decodes=io+mem,owns=io+mem,locks=none\n'+
'[    0.244069] vgaarb: loaded\n'+
'[    0.244572] vgaarb: bridge control possible 0000:00:02.0\n'+
'[    0.248195] SCSI subsystem initialized\n'+
'[    0.248858] libata version 3.00 loaded.\n'+
'[    0.248883] ACPI: bus type USB registered\n'+
'[    0.249513] usbcore: registered new interface driver usbfs\n'+
'[    0.250235] usbcore: registered new interface driver hub\n'+
'[    0.250967] usbcore: registered new device driver usb\n'+
'[    0.252295] PCI: Using ACPI for IRQ routing\n'+
'[    0.253009] PCI: pci_cache_line_size set to 64 bytes\n'+
'[    0.253520] e820: reserve RAM buffer [mem 0x0009fc00-0x0009ffff]\n'+
'[    0.253527] e820: reserve RAM buffer [mem 0x1fff0000-0x1fffffff]\n'+
'[    0.253629] NetLabel: Initializing\n'+
'[    0.254243] NetLabel:  domain hash size = 128\n'+
'[    0.254938] NetLabel:  protocols = UNLABELED CIPSOv4\n'+
'[    0.255686] NetLabel:  unlabeled traffic allowed by default\n'+
'[    0.256554] Switched to clocksource refined-jiffies\n'+
'[    0.264917] AppArmor: AppArmor Filesystem Enabled\n'+
'[    0.265741] pnp: PnP ACPI init\n'+
'[    0.266704] ACPI: bus type PNP registered\n'+
'[    0.268112] pnp 00:00: Plug and Play ACPI device, IDs PNP0303 (active)\n'+
'[    0.268173] pnp 00:01: [dma 4]\n'+
'[    0.268200] pnp 00:01: Plug and Play ACPI device, IDs PNP0200 (active)\n'+
'[    0.268355] pnp 00:02: Plug and Play ACPI device, IDs PNP0f03 (active)\n'+
'[    0.268410] pnp 00:03: Plug and Play ACPI device, IDs PNP0400 (active)\n'+
'[    0.269613] pnp: PnP ACPI: found 4 devices\n'+
'[    0.272241] ACPI: bus type PNP unregistered\n'+
'[    0.282587] Switched to clocksource acpi_pm\n'+
'[    0.283553] pci_bus 0000:00: resource 4 [io  0x0000-0xffff]\n'+
'[    0.283558] pci_bus 0000:00: resource 5 [mem 0x00000000-0xfffffffff]\n'+
'[    0.283610] NET: Registered protocol family 2\n'+
'[    0.283610] TCP established hash table entries: 4096 (order: 3, 32768 bytes)\n'+
'[    0.283987] TCP bind hash table entries: 4096 (order: 4, 65536 bytes)\n'+
'[    0.286393] TCP: Hash tables configured (established 4096 bind 4096)\n'+
'[    0.287604] TCP: reno registered\n'+
'[    0.288476] UDP hash table entries: 256 (order: 1, 8192 bytes)\n'+
'[    0.289669] UDP-Lite hash table entries: 256 (order: 1, 8192 bytes)\n'+
'[    0.290566] NET: Registered protocol family 1\n'+
'[    0.291307] pci 0000:00:00.0: Limiting direct PCI/PCI transfers\n'+
'[    0.292063] pci 0000:00:01.0: Activating ISA DMA hang workarounds\n'+
'[    0.292867] pci 0000:00:02.0: Video device with shadowed ROM\n'+
'[    0.292953] PCI: CLS 0 bytes, default 64\n'+
'[    0.293070] Trying to unpack rootfs image as initramfs...\n'+
'[    0.448987] Freeing initrd memory: 7116K (ffff88001f179000 - ffff88001f86c000)\n'+
'[    0.450299] platform rtc_cmos: registered platform RTC device (no PNP device found)\n'+
'[    0.451654] microcode: CPU0 sig=0x306a9, pf=0x2, revision=0x19\n'+
'[    0.452062] microcode: Microcode Update Driver: v2.00 <tigran@aivazian.fsnet.co.uk>, Peter Oruba\n'+
'[    0.452062] Scanning for low memory corruption every 60 seconds\n'+
'[    0.455437] Initialise system trusted keyring\n'+
'[    0.456116] audit: initializing netlink socket (disabled)\n'+
'[    0.456732] type=2000 audit(1467101696.455:1): initialized\n'+
'[    0.485781] HugeTLB registered 2 MB page size, pre-allocated 0 pages\n'+
'[    0.487507] zbud: loaded\n'+
'[    0.488474] VFS: Disk quotas dquot_6.5.2\n'+
'[    0.489115] Dquot-cache hash table entries: 512 (order 0, 4096 bytes)\n'+
'[    0.490171] fuse init (API version 7.22)\n'+
'[    0.490834] msgmni has been set to 974\n'+
'[    0.491466] Key type big_key registered\n'+
'[    0.493314] Key type asymmetric registered\n'+
'[    0.493993] Asymmetric key parser "x509" registered\n'+
'[    0.494704] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 252)\n'+
'[    0.495862] io scheduler noop registered\n'+
'[    0.496427] io scheduler deadline registered (default)\n'+
'[    0.497179] io scheduler cfq registered\n'+
'[    0.497395] pci_hotplug: PCI Hot Plug PCI Core version: 0.5\n'+
'[    0.498381] pciehp: PCI Express Hot Plug Controller Driver version: 0.4\n'+
'[    0.499270] ipmi message handler version 39.2\n'+
'[    0.501052] ACPI: Deprecated procfs I/F for AC is loaded, please retry with CONFIG_ACPI_PROCFS_POWER cleared\n'+
'[    0.502789] ACPI: AC Adapter [AC] (on-line)\n'+
'[    0.503953] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input0\n'+
'[    0.504707] ACPI: Power Button [PWRF]\n'+
'[    0.505507] input: Sleep Button as /devices/LNXSYSTM:00/LNXSLPBN:00/input/input1\n'+
'[    0.506836] ACPI: Sleep Button [SLPF]\n'+
'[    0.507594] GHES: HEST is not enabled!\n'+
'[    0.508282] Serial: 8250/16550 driver, 32 ports, IRQ sharing enabled\n'+
'[    0.511184] Linux agpgart interface v0.103\n'+
'[    0.513240] ACPI: Deprecated procfs I/F for battery is loaded, please retry with CONFIG_ACPI_PROCFS_POWER cleared\n'+
'[    0.515323] ACPI: Battery Slot [BAT0] (battery present)\n'+
'[    0.525348] brd: module loaded\n'+
'[    0.527196] loop: module loaded\n'+
'[    0.528147] libphy: Fixed MDIO Bus: probed\n'+
'[    0.528147] tun: Universal TUN/TAP device driver, 1.6\n'+
'[    0.529193] tun: (C) 1999-2004 Max Krasnyansky <maxk@qualcomm.com>\n'+
'[    0.530526] PPP generic driver version 2.4.2\n'+
'[    0.531286] ehci_hcd: USB 2.0 "Enhanced" Host Controller (EHCI) Driver\n'+
'[    0.532166] ehci-pci: EHCI PCI platform driver\n'+
'[    0.533023] ehci-platform: EHCI generic platform driver\n'+
'[    0.535533] ohci_hcd: USB 1.1 "Open" Host Controller (OHCI) Driver\n'+
'[    0.537043] ohci-pci: OHCI PCI platform driver\n'+
'[    0.537842] ohci-platform: OHCI generic platform driver\n'+
'[    0.538640] uhci_hcd: USB Universal Host Controller Interface driver\n'+
'[    0.539506] i8042: PNP: PS/2 Controller [PNP0303:PS2K,PNP0f03:PS2M] at 0x60,0x64 irq 1,12\n'+
'[    0.542651] serio: i8042 KBD port at 0x60,0x64 irq 1\n'+
'[    0.543398] serio: i8042 AUX port at 0x60,0x64 irq 12\n'+
'[    0.544197] mousedev: PS/2 mouse device common for all mice\n'+
'[    0.546324] input: AT Translated Set 2 keyboard as /devices/platform/i8042/serio0/input/input2\n'+
'[    0.548396] rtc_cmos rtc_cmos: rtc core: registered rtc_cmos as rtc0\n'+
'[    0.549411] rtc_cmos rtc_cmos: alarms up to one day, 114 bytes nvram\n'+
'[    0.550354] device-mapper: uevent: version 1.0.3\n'+
'[    0.552181] device-mapper: ioctl: 4.27.0-ioctl (2013-10-30) initialised: dm-devel@redhat.com\n'+
'[    0.553709] ledtrig-cpu: registered to indicate activity on CPUs\n'+
'[    0.554776] TCP: cubic registered\n'+
'[    0.555773] NET: Registered protocol family 10\n'+
'[    0.557131] NET: Registered protocol family 17\n'+
'[    0.557841] Key type dns_resolver registered\n'+
'[    0.558678] Loading compiled-in X.509 certificates\n'+
'[    0.561284] Loaded X.509 cert "Magrathea: Glacier signing key: eb178a95d58f38dba12bad4c52c4257e44d6ab5b"\n'+
'[    0.563562] registered taskstats version 1\n'+
'[    0.569267] Key type trusted registered\n'+
'[    0.577199] Key type encrypted registered\n'+
'[    0.578173] AppArmor: AppArmor sha1 policy hashing enabled\n'+
'[    0.579254] IMA: No TPM chip found, activating TPM-bypass!\n'+
'[    0.580447] regulator-dummy: disabling\n'+
'[    0.581146]   Magic number: 4:120:221\n'+
'[    0.581941] rtc_cmos rtc_cmos: setting system clock to 2016-06-28 08:14:57 UTC (1467101697)\n'+
'[    0.583288] BIOS EDD facility v0.16 2004-Jun-25, 0 devices found\n'+
'[    0.584084] EDD information not available.\n'+
'[    0.584959] PM: Hibernation image not present or could not be loaded.\n'+
'[    0.585728] Freeing unused kernel memory: 1336K (ffffffff81d20000 - ffffffff81e6e000)\n'+
'[    0.586973] Write protecting the kernel read-only data: 12288k\n'+
'[    0.588014] Freeing unused kernel memory: 764K (ffff880001741000 - ffff880001800000)\n'+
'[    0.591971] Freeing unused kernel memory: 680K (ffff880001b56000 - ffff880001c00000)\n'+
'[    0.612469] systemd-udevd[92]: starting version 204\n'+
'[    0.646526] ahci 0000:00:0d.0: version 3.0\n'+
'[    0.647156] ahci 0000:00:0d.0: SSS flag set, parallel bus scan disabled\n'+
'[    0.648198] ahci 0000:00:0d.0: AHCI 0001.0100 32 slots 1 ports 3 Gbps 0x1 impl SATA mode\n'+
'[    0.649442] ahci 0000:00:0d.0: flags: 64bit ncq stag only ccc\n'+
'[    0.655491] e1000: Intel(R) PRO/1000 Network Driver - version 7.3.21-k8-NAPI\n'+
'[    0.657626] e1000: Copyright (c) 1999-2006 Intel Corporation.\n'+
'[    0.672010] scsi0 : ahci\n'+
'[    0.672147] ata1: SATA max UDMA/133 abar m8192@0xf0840000 port 0xf0840100 irq 21\n'+
'[    1.135094] input: ImExPS/2 Generic Explorer Mouse as /devices/platform/i8042/serio1/input/input4\n'+
'[    1.156778] e1000 0000:00:03.0 eth0: (PCI:33MHz:32-bit) 08:00:27:8f:dc:e2\n'+
'[    1.157705] e1000 0000:00:03.0 eth0: Intel(R) PRO/1000 Network Connection\n'+
'[    1.573439] ata1: SATA link up 3.0 Gbps (SStatus 123 SControl 300)\n'+
'[    1.575169] tsc: Refined TSC clocksource calibration: 2293.958 MHz\n'+
'[    1.577128] ata1.00: ATA-6: VBOX HARDDISK, 1.0, max UDMA/133\n'+
'[    1.578160] ata1.00: 83886080 sectors, multi 128: LBA48 NCQ (depth 31/32)\n'+
'[    1.579285] ata1.00: configured for UDMA/133\n'+
'[    1.580083] scsi 0:0:0:0: Direct-Access     ATA      VBOX HARDDISK    1.0  PQ: 0 ANSI: 5\n'+
'[    1.582157] sd 0:0:0:0: [sda] 83886080 512-byte logical blocks: (42.9 GB/40.0 GiB)\n'+
'[    1.583565] sd 0:0:0:0: [sda] Write Protect is off\n'+
'[    1.584423] sd 0:0:0:0: [sda] Mode Sense: 00 3a 00 00\n'+
'[    1.584821] sd 0:0:0:0: Attached scsi generic sg0 type 0\n'+
'[    1.586069] sd 0:0:0:0: [sda] Write cache: enabled, read cache: enabled, doesn"t support DPO or FUA\n'+
'[    1.591321]  sda: sda1\n'+
'[    1.593198] sd 0:0:0:0: [sda] Attached SCSI disk\n'+
'[    1.618506] e1000 0000:00:08.0 eth1: (PCI:33MHz:32-bit) 08:00:27:2d:27:3e\n'+
'[    1.619337] e1000 0000:00:08.0 eth1: Intel(R) PRO/1000 Network Connection\n'+
'[    2.576870] Switched to clocksource tsc\n'+
'[    3.138855] EXT4-fs (sda1): mounted filesystem with ordered data mode. Opts: (null)\n'+
'[    3.325937] random: init urandom read with 37 bits of entropy available\n'+
'[    3.664871] EXT4-fs (sda1): re-mounted. Opts: (null)\n'+
'[    4.912469] IPv6: ADDRCONF(NETDEV_UP): eth0: link is not ready\n'+
'[    4.912469] IPv6: ADDRCONF(NETDEV_UP): eth1: link is not ready\n'+
'[    4.918178] IPv6: ADDRCONF(NETDEV_UP): lo: link is not ready\n'+
'[    4.918184] IPv6: ADDRCONF(NETDEV_UP): eth0: link is not ready\n'+
'[    4.918187] IPv6: ADDRCONF(NETDEV_UP): eth1: link is not ready\n'+
'[    4.996752] systemd-udevd[401]: starting version 204\n'+
'[    5.138072] vboxvideo: module verification failed: signature and/or  required key missing - tainting kernel\n'+
'[    5.138093] vboxvideo: Unknown symbol drm_open (err 0)\n'+
'[    5.138098] vboxvideo: Unknown symbol drm_poll (err 0)\n'+
'[    5.138101] vboxvideo: Unknown symbol drm_pci_init (err 0)\n'+
'[    5.138107] vboxvideo: Unknown symbol drm_ioctl (err 0)\n'+
'[    5.138110] vboxvideo: Unknown symbol drm_mmap (err 0)\n'+
'[    5.138113] vboxvideo: Unknown symbol drm_pci_exit (err 0)\n'+
'[    5.138116] vboxvideo: Unknown symbol drm_release (err 0)\n'+
'[    5.205295] type=1400 audit(1467101702.118:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/sbin/dhclient" pid=435 comm="apparmor_parser"\n'+
'[    5.205301] type=1400 audit(1467101702.118:3): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=435 comm="apparmor_parser"\n'+
'[    5.205305] type=1400 audit(1467101702.118:4): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=435 comm="apparmor_parser"\n'+
'[    5.205663] type=1400 audit(1467101702.118:5): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=435 comm="apparmor_parser"\n'+
'[    5.205668] type=1400 audit(1467101702.118:6): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=435 comm="apparmor_parser"\n'+
'[    5.205857] type=1400 audit(1467101702.118:7): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=435 comm="apparmor_parser"\n'+
'[    5.206423] type=1400 audit(1467101702.118:8): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/sbin/dhclient" pid=432 comm="apparmor_parser"\n'+
'[    5.206427] type=1400 audit(1467101702.118:9): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=432 comm="apparmor_parser"\n'+
'[    5.206430] type=1400 audit(1467101702.118:10): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=432 comm="apparmor_parser"\n'+
'[    5.217392] input: Unspecified device as /devices/pci0000:00/0000:00:04.0/input/input5\n'+
'[    5.220922] vboxguest: misc device minor 57, IRQ 20, I/O port d020, MMIO at 00000000f0400000 (size 0x400000)\n'+
'[    5.220929] vboxguest: Successfully loaded version 4.3.36_Ubuntu (interface 0x00010004)\n'+
'[    5.261990] e1000: eth1 NIC Link is Up 1000 Mbps Full Duplex, Flow Control: RX\n'+
'[    5.274124] IPv6: ADDRCONF(NETDEV_UP): eth1: link is not ready\n'+
'[    5.274142] IPv6: ADDRCONF(NETDEV_CHANGE): eth1: link becomes ready\n'+
'[    5.310096] IPv6: ADDRCONF(NETDEV_UP): eth0: link is not ready\n'+
'[    5.310600] e1000: eth0 NIC Link is Up 1000 Mbps Full Duplex, Flow Control: RX\n'+
'[    5.317145] IPv6: ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready\n'+
'[    5.343631] parport_pc 00:03: reported by Plug and Play ACPI\n'+
'[    5.760093] random: nonblocking pool is initialized\n'+
'[    5.789041] ppdev: user-space parallel port driver\n'+
'[    6.430086] init: Failed to obtain startpar-bridge instance: Unknown parameter: INSTANCE\n'+
'[    7.938430] FS-Cache: Loaded\n'+
'[    7.978941] RPC: Registered named UNIX socket transport module.\n'+
'[    7.978944] RPC: Registered udp transport module.\n'+
'[    7.978945] RPC: Registered tcp transport module.\n'+
'[    7.978946] RPC: Registered tcp NFSv4.1 backchannel transport module.\n'+
'[    8.009765] FS-Cache: Netfs "nfs" registered for caching\n'+
'[    8.077860] Installing knfsd (copyright (C) 1996 okir@monad.swb.de).\n'+
'[    8.174799] init: failsafe main process (777) killed by TERM signal\n'+
'[    8.585201] audit_printk_skb: 9 callbacks suppressed\n'+
'[    8.585205] type=1400 audit(1467101705.498:14): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/sbin/dhclient" pid=936 comm="apparmor_parser"\n'+
'[    8.585210] type=1400 audit(1467101705.498:15): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=936 comm="apparmor_parser"\n'+
'[    8.585214] type=1400 audit(1467101705.498:16): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=936 comm="apparmor_parser"\n'+
'[    8.585585] type=1400 audit(1467101705.498:17): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=936 comm="apparmor_parser"\n'+
'[    8.585589] type=1400 audit(1467101705.498:18): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=936 comm="apparmor_parser"\n'+
'[    8.585792] type=1400 audit(1467101705.498:19): apparmor="STATUS" operation="profile_replace" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=936 comm="apparmor_parser"\n'+
'[    8.599371] type=1400 audit(1467101705.510:20): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/tcpdump" pid=938 comm="apparmor_parser"\n'+
'[    8.653154] vboxvideo: Unknown symbol drm_open (err 0)\n'+
'[    8.653160] vboxvideo: Unknown symbol drm_poll (err 0)\n'+
'[    8.653163] vboxvideo: Unknown symbol drm_pci_init (err 0)\n'+
'[    8.653168] vboxvideo: Unknown symbol drm_ioctl (err 0)\n'+
'[    8.653171] vboxvideo: Unknown symbol drm_mmap (err 0)\n'+
'[    8.653174] vboxvideo: Unknown symbol drm_pci_exit (err 0)\n'+
'[    8.653177] vboxvideo: Unknown symbol drm_release (err 0)\n'+
'[    9.393733] vboxsf: Successfully loaded version 4.3.36_Ubuntu (interface 0x00010004)\n'+
'[    9.414605] VBoxService 4.3.36_Ubuntu r105129 (verbosity: 0) linux.amd64 (Jan 27 2016 11:57:44) release log\n'+
'[    9.414605] 00:00:00.000177 main     Log opened 2016-06-28T08:15:06.332278000Z\n'+
'[    9.418759] 00:00:00.004380 main     OS Product: Linux\n'+
'[    9.419831] 00:00:00.005441 main     OS Release: 3.13.0-87-generic\n'+
'[    9.419916] 00:00:00.005577 main     OS Version: #133-Ubuntu SMP Tue May 24 18:32:09 UTC 2016\n'+
'[    9.419978] 00:00:00.005647 main     OS Service Pack: #133-Ubuntu SMP Tue May 24 18:32:09 UTC 2016\n'+
'[    9.421037] 00:00:00.007781 main     Executable: /usr/sbin/VBoxService\n'+
'[    9.421037] 00:00:00.007784 main     Process ID: 1066\n'+
'[    9.421037] 00:00:00.007785 main     Package type: LINUX_64BITS_GENERIC (OSE)\n'+
'[    9.425319] 00:00:00.010867 main     4.3.36_Ubuntu r105129 started. Verbose level = 0\n'+
'[   12.542752] init: plymouth-upstart-bridge main process ended, respawning\n'+
'[   15.820140] IPv6: ADDRCONF(NETDEV_UP): eth1: link is not ready\n'+
'[   15.822053] e1000: eth1 NIC Link is Up 1000 Mbps Full Duplex, Flow Control: RX\n'+
'[   15.822387] IPv6: ADDRCONF(NETDEV_CHANGE): eth1: link becomes ready\n'
var stream_array = stream_message.split('\n');
stream_counter=0;
function Stream(){
  $("#stream_text").append(stream_array[stream_counter]+'</br>');
  stream_counter++;
  if(stream_counter === stream_array.length){
    stream_counter=0;
  }
  if($(".screen").height() <= $("#stream_text").height()){
    clearInterval(stream_interval);
  }
}
stream_interval = setInterval(Stream,1000);
