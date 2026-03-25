# What's is operating system(OS)

An Operating System is a computer program that manages the resources of a computer. It accepts keyboard or mouse inputs from users and displays the results of the actions, and allows the user to run applications or communicate with other computers via networked connections.

Operating systems perform the following important functions: • 1. Processor management, that is, the assignment of a processor to different tasks being performed by the computer system. • 2. Memory management, that is, allocation of main memory and other storage areas to the system programs as well as user programs and data. • 3. Input/output management, that is, coordination and assignment of the different output and input devices while one or more programs are being executed. • 4. File management, that is, the storage of file of various storage devices to another. It also allows all files to be easily changed and modified through the use of text editors or some other file manipulation routines.

#Type of operating system(OS)

Windows (Windows 98, XP, Vista, 7, 8), Macintosh OS X, and the many versions of Linux and Unix. DOS is still used for some applications, and there are many other special-purpose operating systems (Embedded Linux). Android is a mobile operating system (OS) based on the Linux kernel and currently developed by Google.


# Linux operating system(OS)


UNIX is a multitasking and multiuser operating system designed to provide a stable, secure, and efficient computing environment. It was originally developed at AT&T Bell Labs and later became the foundation for many modern operating systems.
 

#Linux Basic

How Linux works:

- The core components of Linux (kernel, user space, init/systemd)
- How processes are created and managed
- What systemd does and why it matters


1. core components of Linux

The Linux operating system is composed of several key components that work together to provide a powerful computing environment. These components include the kernel, shell, system utilities, and application software. Each component plays a specific role in managing system resources, providing an interface between hardware and user space applications, and enabling communication between software and hardware. Understanding these components is essential for anyone looking to use, manage, or develop on a Linux system.


| Kernel - The core of Linux; manages hardware, memory, processes, and system resources.
| Shell - Command-line interface that interprets user commands and passes them to the kernel.
| File System - Organises and stores data in directories and files, ensuring structured access.
| System Utilities - Essential tools for system management (e.g., `ls`, `cp`, `ps`, `grep`).
| Applications - End-user programs like browsers, text editors, and databases running on top of Linux.
| Hardware Layer - Physical devices (CPU, memory, disk, network cards) that the kernel controls. 
| Process Management - Handles scheduling, execution, and termination of processes.
| Memory Management - Allocates and tracks physical/virtual memory for efficient performance. 
| Networking - Provides communication via protocols, sockets, and drivers for connectivity. 
| Storage Management Manages file systems, I/O operations, and data persistence. 



2. How Process Creation Works in Linux

- Every process in Linux starts from another process (except the very first process, init or system)
- When you run a command (e.g., ls), the shell itself is a process that creates a new child process to execute that command.
- fork() duplicates the calling process’s address space, creating a child process.
- Both parent and child continue execution from the point after the fork() call.

Return values differ:
- Child process → fork() returns 0.
- Parent process → fork() returns the PID of the child.
- Error → fork() returns -1.
- Each process gets a unique Process ID (PID).
- The parent process is tracked via Parent Process ID (PPID).
- After fork(), the child process often calls exec() (e.g., execve) to replace its memory space with a new program.
- This allows the child to run a completely different program than the parent.
- Process runs until completion or termination.
- Parent may call wait() to collect the child’s exit status.
- Once finished, the process is removed from the process table
- Process creation = fork + exec model.
- Parent process spawns child → child can either continue the same program or load a new one.
- PID/PPID system ensures tracking and prevents duplication.
- Shell commands rely on this mechanism every time you run something.


Example in Real Life
- You type ls in the shell.
- The shell process forks a child.
- The child calls exec() to load /bin/ls.
- The child runs ls and prints the directory listing.
- The child exits, and the shell (parent) regains control, waiting for your next command.


3. What systemd does and why it matters

Systemd matters because it makes Linux systems faster, more reliable, and easier to manage.

Example in Real Life:
 

When you type the command:  systemctl restart nginx


What Systemd Does
- Boot Management → Initializes the system after the kernel loads.
- Service Control → Starts, stops, restarts, and monitors services using systemctl.
- Parallel Startup → Launches services simultaneously, speeding up boot time.
- Dependency Handling → Ensures services start in the right order via unit files.
- Logging → Collects logs with journald for easier troubleshooting.
- Resource Management → Uses cgroups to control CPU, memory, and I/O per service.
- Timers & Scheduling → Replaces cron jobs with flexible timers.
- Socket Activation → Starts services only when needed, saving resources.

Why It Matters
- Performance → Faster boot and efficient resource use.
- Reliability → Restarts failed services automatically.
- Consistency → Provides a unified way to manage services across distributions.
- Scalability → Works well for servers, containers, and large deployments.
- Debugging → Integrated logging makes troubleshooting straightforward.


Systemd:
- Finds the unit file for nginx.
- Stops the running service.
- Starts it again, ensuring dependencies (like networking) are active.
- Logs the event in journalctl.

- At the top, Systemd runs as PID1 (the very first process after the kernel).
- It reads unit files (service, socket, device, mount, target definitions).
- These units are grouped into targets (like multi-user.target or graphical.target) that define system states.
- systemctl is the command-line tool you use to control these units.
- journald collects logs from all services for centralized troubleshooting.
- cgroups manage resources (CPU, memory, I/O) per service.
- timers replace cron jobs for scheduling tasks.
- socket activation ensures services only start when needed, improving efficiency.
This layered view shows how Systemd orchestrates the entire lifecycle of services and system states, making Linux faster, more reliable, and easier to manage.



