# EKANS ransomware
EKANS ransomware string decrypter

based on https://github.com/losersqueeze/EKANS-ransomware and https://gist.github.com/W3ndige/0e741c4e04555e67b2219b1a2885852c

tested only on https://www.virustotal.com/gui/file/edef8b955468236c6323e9019abb10c324c27b4f5667bc3f85f3a097b2e5159a

Strings extracted:
```
key pos: 0x618080 str pos: 0x61801a length: 6
hangup

key pos: 0x619894 str pos: 0x619735 length: 9
interrupt

key pos: 0x617a80 str pos: 0x617a34 length: 4
quit

key pos: 0x624625 str pos: 0x62471c length: 19
illegal instruction

key pos: 0x625f51 str pos: 0x626134 length: 21
trace/breakpoint trap

key pos: 0x618673 str pos: 0x618936 length: 7
aborted

key pos: 0x61925b str pos: 0x61940b length: 9
bus error

key pos: 0x627efe str pos: 0x62834e length: 24
floating point exception

key pos: 0x618212 str pos: 0x6181be length: 6
killed

key pos: 0x625e94 str pos: 0x62615e length: 21
user defined signal 1

key pos: 0x62371a str pos: 0x623492 length: 18
segmentation fault

key pos: 0x625f3c str pos: 0x62611f length: 21
user defined signal 2

key pos: 0x61bf66 str pos: 0x61c969 length: 11
broken pipe

key pos: 0x61ba6a str pos: 0x61c2ec length: 11
alarm clock

key pos: 0x61a31e str pos: 0x61aecc length: 10
terminated

key pos: 0x62395a str pos: 0x6239d8 length: 18
1.3.6.1.5.5.7.3.1

key pos: 0x627ae2 str pos: 0x6272e3 length: 23
1.3.6.1.4.1.311.10.3.3

key pos: 0x6265ce str pos: 0x626912 length: 22
2.16.840.1.113730.4.1

key pos: 0x61d387 str pos: 0x61eb87 length: 12
advapi32.dll

key pos: 0x61ea07 str pos: 0x61d55b length: 12
kernel32.dll

key pos: 0x61b87b str pos: 0x61c580 length: 11
shell32.dll

key pos: 0x61c927 str pos: 0x61bc59 length: 11
userenv.dll

key pos: 0x61b6fa str pos: 0x61c4fc length: 11
mswsock.dll

key pos: 0x61c205 str pos: 0x61bf7c length: 11
crypt32.dll

key pos: 0x61a45e str pos: 0x61ad46 length: 10
user32.dll

key pos: 0x619666 str pos: 0x619ccc length: 9
ole32.dll

key pos: 0x619831 str pos: 0x6198dc length: 9
ntdll.dll

key pos: 0x6192ac str pos: 0x6191f8 length: 9
psapi.dll

key pos: 0x619e5a str pos: 0x61a2a6 length: 10
ws2_32.dll

key pos: 0x61a6ca str pos: 0x61a936 length: 10
dnsapi.dll

key pos: 0x61e11f str pos: 0x61de07 length: 12
iphlpapi.dll

key pos: 0x61c688 str pos: 0x61b8f4 length: 11
secur32.dll

key pos: 0x61cdc3 str pos: 0x61d0c3 length: 12
netapi32.dll

key pos: 0x61da17 str pos: 0x61e773 length: 12
wtsapi32.dll

key pos: 0x6252b8 str pos: 0x625510 length: 20
RegisterEventSourceW

key pos: 0x626188 str pos: 0x626023 length: 21
DeregisterEventSource

key pos: 0x61d4fb str pos: 0x61d1a7 length: 12
ReportEventW

key pos: 0x6204d7 str pos: 0x62081f length: 14
OpenSCManagerW

key pos: 0x62346e str pos: 0x623c96 length: 18
CloseServiceHandle

key pos: 0x620547 str pos: 0x620ddd length: 14
CreateServiceW

key pos: 0x61de2b str pos: 0x61e3e3 length: 12
OpenServiceW

key pos: 0x61f903 str pos: 0x61f679 length: 13
DeleteService

key pos: 0x61f833 str pos: 0x61f66c length: 13
StartServiceW

key pos: 0x623798 str pos: 0x6236f6 length: 18
QueryServiceStatus

key pos: 0x627acb str pos: 0x6270d2 length: 23
QueryServiceLockStatusW

key pos: 0x620643 str pos: 0x6208ff length: 14
ControlService

key pos: 0x6297e0 str pos: 0x62984c length: 27
StartServiceCtrlDispatcherW

key pos: 0x622420 str pos: 0x622560 length: 16
SetServiceStatus

key pos: 0x625254 str pos: 0x62545c length: 20
ChangeServiceConfigW

key pos: 0x6247ed str pos: 0x6244cf length: 19
QueryServiceConfigW

key pos: 0x625f66 str pos: 0x6260f5 length: 21
ChangeServiceConfig2W

key pos: 0x6254d4 str pos: 0x62527c length: 20
QueryServiceConfig2W

key pos: 0x625c33 str pos: 0x625dad length: 21
EnumServicesStatusExW

key pos: 0x624e80 str pos: 0x6251a0 length: 20
QueryServiceStatusEx

key pos: 0x629667 str pos: 0x62911f length: 26
NotifyServiceStatusChangeW

key pos: 0x61d447 str pos: 0x61cebf length: 12
GetLastError

key pos: 0x61d12f str pos: 0x61d777 length: 12
LoadLibraryW

key pos: 0x6202d1 str pos: 0x620421 length: 14
LoadLibraryExW

key pos: 0x61c3ff str pos: 0x61bf71 length: 11
FreeLibrary

key pos: 0x61fe55 str pos: 0x620af7 length: 14
GetProcAddress

key pos: 0x6238a6 str pos: 0x623f30 length: 18
GetModuleFileNameW

key pos: 0x623816 str pos: 0x623762 length: 18
GetModuleHandleExW

key pos: 0x61a4f4 str pos: 0x61a8c8 length: 10
GetVersion

key pos: 0x620539 str pos: 0x620803 length: 14
FormatMessageW

key pos: 0x61c953 str pos: 0x61bba9 length: 11
ExitProcess

key pos: 0x620e07 str pos: 0x62059b length: 14
IsWow64Process

key pos: 0x61bacd str pos: 0x61c0f2 length: 11
CreateFileW

key pos: 0x618e68 str pos: 0x618d90 length: 8
ReadFile

key pos: 0x619183 str pos: 0x619ba3 length: 9
WriteFile

key pos: 0x624106 str pos: 0x624d1f length: 19
GetOverlappedResult

key pos: 0x620c71 str pos: 0x61fdc9 length: 14
SetFilePointer

key pos: 0x61bda3 str pos: 0x61c2e1 length: 11
CloseHandle

key pos: 0x61e89f str pos: 0x61d67b length: 12
GetStdHandle

key pos: 0x61d1cb str pos: 0x61d4ef length: 12
SetStdHandle

key pos: 0x620953 str pos: 0x62065f length: 14
FindFirstFileW

key pos: 0x61f387 str pos: 0x61f14b length: 13
FindNextFileW

key pos: 0x6195bb str pos: 0x619a5f length: 9
FindClose

key pos: 0x6291ef str pos: 0x62935b length: 26
GetFileInformationByHandle

key pos: 0x629d41 str pos: 0x62a29d length: 28
GetFileInformationByHandleEx

key pos: 0x6253e4 str pos: 0x6255ec length: 20
GetCurrentDirectoryW

key pos: 0x6253bc str pos: 0x625628 length: 20
SetCurrentDirectoryW

key pos: 0x622600 str pos: 0x622470 length: 16
CreateDirectoryW

key pos: 0x622590 str pos: 0x622440 length: 16
RemoveDirectoryW

key pos: 0x61b7aa str pos: 0x61b38a length: 11
DeleteFileW

key pos: 0x619708 str pos: 0x6199c6 length: 9
MoveFileW

key pos: 0x61be06 str pos: 0x61c4ba length: 11
MoveFileExW

key pos: 0x61afd0 str pos: 0x61a5f8 length: 10
LockFileEx

key pos: 0x61e7bb str pos: 0x61de1f length: 12
UnlockFileEx

key pos: 0x622340 str pos: 0x622910 length: 16
GetComputerNameW

key pos: 0x623bd0 str pos: 0x623a68 length: 18
GetComputerNameExW

key pos: 0x61dff3 str pos: 0x61e5e7 length: 12
SetEndOfFile

key pos: 0x62757e str pos: 0x627608 length: 23
GetSystemTimeAsFileTime

key pos: 0x62ae5b str pos: 0x62adc5 length: 30
GetSystemTimePreciseAsFileTime

key pos: 0x6265a2 str pos: 0x626d1c length: 22
GetTimeZoneInformation

key pos: 0x626b90 str pos: 0x626a30 length: 22
CreateIoCompletionPort

key pos: 0x6287e4 str pos: 0x628893 length: 25
GetQueuedCompletionStatus

key pos: 0x628efd str pos: 0x62909d length: 26
PostQueuedCompletionStatus

key pos: 0x618a10 str pos: 0x619040 length: 8
CancelIo

key pos: 0x61a986 str pos: 0x61a53a length: 10
CancelIoEx

key pos: 0x620bd7 str pos: 0x61ff35 length: 14
CreateProcessW

key pos: 0x61b726 str pos: 0x61b395 length: 11
OpenProcess

key pos: 0x61f0c9 str pos: 0x61fbdb length: 13
ShellExecuteW

key pos: 0x625524 str pos: 0x6252f4 length: 20
SHGetKnownFolderPath

key pos: 0x621e50 str pos: 0x622670 length: 16
TerminateProcess

key pos: 0x623c84 str pos: 0x62373e length: 18
GetExitCodeProcess

key pos: 0x620ec8 str pos: 0x621c7e length: 15
GetStartupInfoW

key pos: 0x6216ed str pos: 0x6219f9 length: 15
GetProcessTimes

key pos: 0x621639 str pos: 0x621954 length: 15
DuplicateHandle

key pos: 0x624437 str pos: 0x6241d7 length: 19
WaitForSingleObject

key pos: 0x6268a4 str pos: 0x626c40 length: 22
WaitForMultipleObjects

key pos: 0x61e41f str pos: 0x61dd17 length: 12
GetTempPathW

key pos: 0x61a1ac str pos: 0x61a3fa length: 10
CreatePipe

key pos: 0x61c27e str pos: 0x61bd98 length: 11
GetFileType

key pos: 0x625470 str pos: 0x6252a4 length: 20
CryptAcquireContextW

key pos: 0x6240f3 str pos: 0x624d58 length: 19
CryptReleaseContext

key pos: 0x620793 str pos: 0x6209ed length: 14
CryptGenRandom

key pos: 0x626b7a str pos: 0x626a46 length: 22
GetEnvironmentStringsW

key pos: 0x6275da str pos: 0x6276a9 length: 23
FreeEnvironmentStringsW

key pos: 0x6274dd str pos: 0x6276d7 length: 23
GetEnvironmentVariableW

key pos: 0x627b27 str pos: 0x627522 length: 23
SetEnvironmentVariableW

key pos: 0x626ba6 str pos: 0x626a1a length: 22
CreateEnvironmentBlock

key pos: 0x62712e str pos: 0x627ab4 length: 23
DestroyEnvironmentBlock

key pos: 0x62067b str pos: 0x620937 length: 14
GetTickCount64

key pos: 0x61bdae str pos: 0x61c457 length: 11
SetFileTime

key pos: 0x623b9a str pos: 0x62396c length: 18
GetFileAttributesW

key pos: 0x623d5c str pos: 0x6234ec length: 18
SetFileAttributesW

key pos: 0x6253f8 str pos: 0x6255b0 length: 20
GetFileAttributesExW

key pos: 0x6211b6 str pos: 0x62134b length: 15
GetCommandLineW

key pos: 0x6234da str pos: 0x623f0c length: 18
CommandLineToArgvW

key pos: 0x619630 str pos: 0x619c8d length: 9
LocalFree

key pos: 0x625484 str pos: 0x625330 length: 20
SetHandleInformation

key pos: 0x622100 str pos: 0x622260 length: 16
FlushFileBuffers

key pos: 0x621d90 str pos: 0x622680 length: 16
GetFullPathNameW

key pos: 0x622550 str pos: 0x622370 length: 16
GetLongPathNameW

key pos: 0x6229c9 str pos: 0x62314a length: 17
GetShortPathNameW

key pos: 0x623bbe str pos: 0x623a20 length: 18
CreateFileMappingW

key pos: 0x61f020 str pos: 0x61fae4 length: 13
MapViewOfFile

key pos: 0x621468 str pos: 0x621846 length: 15
UnmapViewOfFile

key pos: 0x621111 str pos: 0x62125b length: 15
FlushViewOfFile

key pos: 0x61bdb9 str pos: 0x61c3f4 length: 11
VirtualLock

key pos: 0x61f4f3 str pos: 0x61f85a length: 13
VirtualUnlock

key pos: 0x61cb77 str pos: 0x61edeb length: 12
VirtualAlloc

key pos: 0x61be53 str pos: 0x61c231 length: 11
VirtualFree

key pos: 0x620bc9 str pos: 0x61ffc1 length: 14
VirtualProtect

key pos: 0x61ce6b str pos: 0x61d5df length: 12
TransmitFile

key pos: 0x625ea9 str pos: 0x6260b6 length: 21
ReadDirectoryChangesW

key pos: 0x62513c str pos: 0x625218 length: 20
CertOpenSystemStoreW

key pos: 0x61f6c7 str pos: 0x61f992 length: 13
CertOpenStore

key pos: 0x629a4d str pos: 0x6296d2 length: 27
CertEnumCertificatesInStore

key pos: 0x62bd27 str pos: 0x62b7c7 length: 32
CertAddCertificateContextToStore

key pos: 0x6202a7 str pos: 0x62043d length: 14
CertCloseStore

key pos: 0x627311 str pos: 0x627453 length: 23
CertGetCertificateChain

key pos: 0x627fee str pos: 0x627ee6 length: 24
CertFreeCertificateChain

key pos: 0x629d95 str pos: 0x62a281 length: 28
CertCreateCertificateContext

key pos: 0x629035 str pos: 0x628f17 length: 26
CertFreeCertificateContext

key pos: 0x62b907 str pos: 0x62b947 length: 32
CertVerifyCertificateChainPolicy

key pos: 0x61fa6f str pos: 0x61f722 length: 13
RegOpenKeyExW

key pos: 0x61c646 str pos: 0x61b26c length: 11
RegCloseKey

key pos: 0x621e60 str pos: 0x622720 length: 16
RegQueryInfoKeyW

key pos: 0x61f6ad str pos: 0x61f9b9 length: 13
RegEnumKeyExW

key pos: 0x6225e0 str pos: 0x6223d0 length: 16
RegQueryValueExW

key pos: 0x62400f str pos: 0x624d0c length: 19
GetCurrentProcessId

key pos: 0x620d27 str pos: 0x61ff43 length: 14
GetConsoleMode

key pos: 0x6206f9 str pos: 0x62091b length: 14
SetConsoleMode

key pos: 0x6292a5 str pos: 0x6291bb length: 26
GetConsoleScreenBufferInfo

key pos: 0x61f7f2 str pos: 0x61f5b6 length: 13
WriteConsoleW

key pos: 0x61ee4b str pos: 0x61dc1b length: 12
ReadConsoleW

key pos: 0x627e9e str pos: 0x627fd6 length: 24
CreateToolhelp32Snapshot

key pos: 0x6218eb str pos: 0x621693 length: 15
Process32FirstW

key pos: 0x6204bb str pos: 0x62082d length: 14
Process32NextW

key pos: 0x61f165 str pos: 0x61f3e2 length: 13
Thread32First

key pos: 0x61d687 str pos: 0x61d003 length: 12
Thread32Next

key pos: 0x6215b2 str pos: 0x6218a0 length: 15
DeviceIoControl

key pos: 0x624554 str pos: 0x624800 length: 19
CreateSymbolicLinkW

key pos: 0x621729 str pos: 0x621a08 length: 15
CreateHardLinkW

key pos: 0x623d80 str pos: 0x6234a4 length: 18
GetCurrentThreadId

key pos: 0x61e84b str pos: 0x61dfe7 length: 12
CreateEventW

key pos: 0x62088f str pos: 0x6205a9 length: 14
CreateEventExW

key pos: 0x61ac74 str pos: 0x61a3d2 length: 10
OpenEventW

key pos: 0x618cf0 str pos: 0x618c00 length: 8
SetEvent

key pos: 0x61a72e str pos: 0x61abca length: 10
ResetEvent

key pos: 0x61a01c str pos: 0x61a404 length: 10
PulseEvent

key pos: 0x61e893 str pos: 0x61d6db length: 12
CreateMutexW

key pos: 0x620333 str pos: 0x620a87 length: 14
CreateMutexExW

key pos: 0x61a918 str pos: 0x61a544 length: 10
OpenMutexW

key pos: 0x61d6b7 str pos: 0x61cf73 length: 12
ReleaseMutex

key pos: 0x618872 str pos: 0x618451 length: 7
SleepEx

key pos: 0x622270 str pos: 0x622150 length: 16
CreateJobObjectW

key pos: 0x627e3e str pos: 0x627fa6 length: 24
AssignProcessToJobObject

key pos: 0x6237ce str pos: 0x623522 length: 18
TerminateJobObject

key pos: 0x61eb27 str pos: 0x61cd27 length: 12
SetErrorMode

key pos: 0x61cc5b str pos: 0x61e8f3 length: 12
ResumeThread

key pos: 0x6221c0 str pos: 0x621df0 length: 16
SetPriorityClass

key pos: 0x622580 str pos: 0x6223c0 length: 16
GetPriorityClass

key pos: 0x62767b str pos: 0x6275c3 length: 23
SetInformationJobObject

key pos: 0x627f2e str pos: 0x628036 length: 24
GenerateConsoleCtrlEvent

key pos: 0x61d63f str pos: 0x61d0db length: 12
GetProcessId

key pos: 0x61a94a str pos: 0x61a508 length: 10
OpenThread

key pos: 0x62746a str pos: 0x6276c0 length: 23
SetProcessPriorityBoost

key pos: 0x6223f0 str pos: 0x6225b0 length: 16
DefineDosDeviceW

key pos: 0x6275f1 str pos: 0x6274f4 length: 23
DeleteVolumeMountPointW

key pos: 0x622120 str pos: 0x622280 length: 16
FindFirstVolumeW

key pos: 0x62928b str pos: 0x629153 length: 26
FindFirstVolumeMountPointW

key pos: 0x621567 str pos: 0x621927 length: 15
FindNextVolumeW

key pos: 0x62866d str pos: 0x628622 length: 25
FindNextVolumeMountPointW

key pos: 0x621891 str pos: 0x6215fd length: 15
FindVolumeClose

key pos: 0x6287b2 str pos: 0x6288ac length: 25
FindVolumeMountPointClose

key pos: 0x624898 str pos: 0x62465e length: 19
GetDiskFreeSpaceExW

key pos: 0x61efd2 str pos: 0x61fbe8 length: 13
GetDriveTypeW

key pos: 0x622500 str pos: 0x6222f0 length: 16
GetLogicalDrives

key pos: 0x62740e str pos: 0x6277a6 length: 23
GetLogicalDriveStringsW

key pos: 0x625e7f str pos: 0x626038 length: 21
GetVolumeInformationW

key pos: 0x62a6b6 str pos: 0x62a608 length: 29
GetVolumeInformationByHandleW

key pos: 0x62beae str pos: 0x62be8d length: 33
GetVolumeNameForVolumeMountPointW

key pos: 0x62383a str pos: 0x623708 length: 18
GetVolumePathNameW

key pos: 0x62b967 str pos: 0x62b927 length: 32
GetVolumePathNamesForVolumeNameW

key pos: 0x6217ec str pos: 0x6213f0 length: 15
QueryDosDeviceW

key pos: 0x6215d0 str pos: 0x621990 length: 15
SetVolumeLabelW

key pos: 0x624ea8 str pos: 0x625678 length: 20
SetVolumeMountPointW

key pos: 0x61c39c str pos: 0x61bf5b length: 11
MessageBoxW

key pos: 0x61f409 str pos: 0x61f2b7 length: 13
ExitWindowsEx

key pos: 0x6287cb str pos: 0x6288f7 length: 25
InitiateSystemShutdownExW

key pos: 0x62a035 str pos: 0x629f39 length: 28
SetProcessShutdownParameters

key pos: 0x62a089 str pos: 0x62a0dd length: 28
GetProcessShutdownParameters

key pos: 0x621288 str pos: 0x6210b7 length: 15
CLSIDFromString

key pos: 0x621003 str pos: 0x62133c length: 15
StringFromGUID2

key pos: 0x61dc9f str pos: 0x61e413 length: 12
CoCreateGuid

key pos: 0x61fdaf str pos: 0x61f5c3 length: 13
CoTaskMemFree

key pos: 0x61f78a str pos: 0x61f944 length: 13
RtlGetVersion

key pos: 0x626be8 str pos: 0x626a9e length: 22
RtlGetNtVersionNumbers

key pos: 0x62b0ef str pos: 0x62acd5 length: 30
GetProcessPreferredUILanguages

key pos: 0x62a781 str pos: 0x62a886 length: 29
GetThreadPreferredUILanguages

key pos: 0x6298d3 str pos: 0x629990 length: 27
GetUserPreferredUILanguages

key pos: 0x62a6f0 str pos: 0x62a577 length: 29
GetSystemPreferredUILanguages

key pos: 0x61f61e str pos: 0x61f8b5 length: 13
EnumProcesses

key pos: 0x61a562 str pos: 0x61aa44 length: 10
WSAStartup

key pos: 0x619f54 str pos: 0x61ad96 length: 10
WSACleanup

key pos: 0x618d50 str pos: 0x618ee0 length: 8
WSAIoctl

key pos: 0x6181b2 str pos: 0x618224 length: 6
socket

key pos: 0x61817c str pos: 0x618290 length: 6
sendto

key pos: 0x618de0 str pos: 0x618ec8 length: 8
recvfrom

key pos: 0x61ab34 str pos: 0x61a684 length: 10
setsockopt

key pos: 0x61af30 str pos: 0x61a440 length: 10
getsockopt

key pos: 0x61795c str pos: 0x6178d8 length: 4
bind

key pos: 0x6187d1 str pos: 0x6186b9 length: 7
connect

key pos: 0x61b802 str pos: 0x61c53e length: 11
getsockname

key pos: 0x61c512 str pos: 0x61b818 length: 11
getpeername

key pos: 0x6181d6 str pos: 0x618206 length: 6
listen

key pos: 0x618ca8 str pos: 0x6190b8 length: 8
shutdown

key pos: 0x61c35a str pos: 0x61bb3b length: 11
closesocket

key pos: 0x618db0 str pos: 0x618eb8 length: 8
AcceptEx

key pos: 0x6252cc str pos: 0x6254c0 length: 20
GetAcceptExSockaddrs

key pos: 0x618706 str pos: 0x6187fb length: 7
WSARecv

key pos: 0x61850e str pos: 0x618657 length: 7
WSASend

key pos: 0x61c5b7 str pos: 0x61b1bc length: 11
WSARecvFrom

key pos: 0x6197bc str pos: 0x619a05 length: 9
WSASendTo

key pos: 0x61f6ba str pos: 0x61fd54 length: 13
gethostbyname

key pos: 0x61f416 str pos: 0x61fc1c length: 13
getservbyname

key pos: 0x617db4 str pos: 0x617f44 length: 5
ntohs

key pos: 0x620707 str pos: 0x620857 length: 14
getprotobyname

key pos: 0x619f22 str pos: 0x61af4e length: 10
DnsQuery_W

key pos: 0x62307e str pos: 0x6229b8 length: 17
DnsRecordListFree

key pos: 0x622290 str pos: 0x622660 length: 16
DnsNameCompare_W

key pos: 0x61e3ef str pos: 0x61dd23 length: 12
GetAddrInfoW

key pos: 0x61f937 str pos: 0x61f6a0 length: 13
FreeAddrInfoW

key pos: 0x61af1c str pos: 0x619f4a length: 10
GetIfEntry

key pos: 0x62126a str pos: 0x6210c6 length: 15
GetAdaptersInfo

key pos: 0x62c50f str pos: 0x62c333 length: 34
SetFileCompletionNotificationModes

key pos: 0x622f7f str pos: 0x622de7 length: 17
WSAEnumProtocolsW

key pos: 0x6254e8 str pos: 0x625394 length: 20
GetAdaptersAddresses

key pos: 0x618062 str pos: 0x618182 length: 6
GetACP

key pos: 0x624bc9 str pos: 0x6240cd length: 19
MultiByteToWideChar

key pos: 0x620b91 str pos: 0x620031 length: 14
TranslateNameW

key pos: 0x62083b str pos: 0x6205b7 length: 14
GetUserNameExW

key pos: 0x620961 str pos: 0x620697 length: 14
NetUserGetInfo

key pos: 0x625aa4 str pos: 0x6262d8 length: 21
NetGetJoinInformation

key pos: 0x621ed0 str pos: 0x622800 length: 16
NetApiBufferFree

key pos: 0x622aea str pos: 0x622d2c length: 17
LookupAccountSidW

key pos: 0x623750 str pos: 0x623db6 length: 18
LookupAccountNameW

key pos: 0x6269c2 str pos: 0x626b22 length: 22
ConvertSidToStringSidW

key pos: 0x626e24 str pos: 0x626610 length: 22
ConvertStringSidToSidW

key pos: 0x61d5a3 str pos: 0x61cf2b length: 12
GetLengthSid

key pos: 0x61839b str pos: 0x61888e length: 7
CopySid

key pos: 0x627b6e str pos: 0x628216 length: 24
AllocateAndInitializeSid

key pos: 0x623510 str pos: 0x623efa length: 18
CreateWellKnownSid

key pos: 0x620395 str pos: 0x6200cb length: 14
IsWellKnownSid

key pos: 0x618355 str pos: 0x61883a length: 7
FreeSid

key pos: 0x618f48 str pos: 0x618e40 length: 8
EqualSid

key pos: 0x62874e str pos: 0x628861 length: 25
GetSidIdentifierAuthority

key pos: 0x627af9 str pos: 0x627117 length: 23
GetSidSubAuthorityCount

key pos: 0x623bf4 str pos: 0x623a44 length: 18
GetSidSubAuthority

key pos: 0x61a0c6 str pos: 0x61a382 length: 10
IsValidSid

key pos: 0x624df4 str pos: 0x6256a0 length: 20
CheckTokenMembership

key pos: 0x621ff0 str pos: 0x622220 length: 16
OpenProcessToken

key pos: 0x621102 str pos: 0x6212c4 length: 15
OpenThreadToken

key pos: 0x6216cf str pos: 0x621a17 length: 15
ImpersonateSelf

key pos: 0x61d627 str pos: 0x61ce9b length: 12
RevertToSelf

key pos: 0x620945 str pos: 0x6206dd length: 14
SetThreadToken

key pos: 0x625e2b str pos: 0x625d6e length: 21
LookupPrivilegeValueW

key pos: 0x626173 str pos: 0x625fba length: 21
AdjustTokenPrivileges

key pos: 0x622f08 str pos: 0x623007 length: 17
AdjustTokenGroups

key pos: 0x624411 str pos: 0x624282 length: 19
GetTokenInformation

key pos: 0x6248be str pos: 0x6245ff length: 19
SetTokenInformation

key pos: 0x622540 str pos: 0x622390 length: 16
DuplicateTokenEx

key pos: 0x627fbe str pos: 0x627e6e length: 24
GetUserProfileDirectoryW

key pos: 0x624b57 str pos: 0x6240a7 length: 19
GetSystemDirectoryW

key pos: 0x624ef8 str pos: 0x6259d4 length: 20
GetWindowsDirectoryW

key pos: 0x62930d str pos: 0x6291d5 length: 26
GetSystemWindowsDirectoryW

key pos: 0x622f4c str pos: 0x622e6f length: 17
WTSQueryUserToken

key pos: 0x625a8f str pos: 0x625dd7 length: 21
WTSEnumerateSessionsW

key pos: 0x61f29d str pos: 0x61f394 length: 13
WTSFreeMemory

key pos: 0x6210e4 str pos: 0x6212a6 length: 15
GetSecurityInfo

key pos: 0x62142c str pos: 0x621819 length: 15
SetSecurityInfo

key pos: 0x626299 str pos: 0x625d98 length: 21
GetNamedSecurityInfoW

key pos: 0x625e16 str pos: 0x625cdb length: 21
SetNamedSecurityInfoW

key pos: 0x627f16 str pos: 0x628006 length: 24
BuildSecurityDescriptorW

key pos: 0x62a131 str pos: 0x629ffd length: 28
InitializeSecurityDescriptor

key pos: 0x629f55 str pos: 0x629fe1 length: 28
GetSecurityDescriptorControl

key pos: 0x628415 str pos: 0x628b68 length: 25
GetSecurityDescriptorDacl

key pos: 0x6288c5 str pos: 0x628799 length: 25
GetSecurityDescriptorSacl

key pos: 0x629341 str pos: 0x629209 length: 26
GetSecurityDescriptorOwner

key pos: 0x6295ff str pos: 0x628dc5 length: 26
GetSecurityDescriptorGroup

key pos: 0x62993f str pos: 0x6298b8 length: 27
GetSecurityDescriptorLength

key pos: 0x62b2b1 str pos: 0x62ad11 length: 30
GetSecurityDescriptorRMControl

key pos: 0x628767 str pos: 0x628848 length: 25
IsValidSecurityDescriptor

key pos: 0x629ec9 str pos: 0x62a019 length: 28
SetSecurityDescriptorControl

key pos: 0x6288de str pos: 0x628780 length: 25
SetSecurityDescriptorDacl

key pos: 0x6283b1 str pos: 0x628cf8 length: 25
SetSecurityDescriptorSacl

key pos: 0x6292d9 str pos: 0x6291a1 length: 26
SetSecurityDescriptorOwner

key pos: 0x628d43 str pos: 0x629597 length: 26
SetSecurityDescriptorGroup

key pos: 0x62af2d str pos: 0x62aed3 length: 30
SetSecurityDescriptorRMControl

key pos: 0x62f8ab str pos: 0x62f8df length: 52
ConvertStringSecurityDescriptorToSecurityDescriptorW

key pos: 0x62f877 str pos: 0x62f80f length: 52
ConvertSecurityDescriptorToStringSecurityDescriptorW

key pos: 0x620689 str pos: 0x62097d length: 14
MakeAbsoluteSD

key pos: 0x6236ae str pos: 0x623828 length: 18
MakeSelfRelativeSD

key pos: 0x6224b0 str pos: 0x622310 length: 16
SetEntriesInAclW

key pos: 0x621576 str pos: 0x621918 length: 15
Failed to load 

key pos: 0x617625 str pos: 0x61757d length: 2
: 

key pos: 0x6213c3 str pos: 0x621210 length: 15
Failed to find 

key pos: 0x6209df str pos: 0x620deb length: 14
 procedure in 

key pos: 0x617627 str pos: 0x617629 length: 2
: 

key pos: 0x617e6d str pos: 0x617deb length: 5
Call 

key pos: 0x62842e str pos: 0x628654 length: 25
 with too many arguments 

key pos: 0x617564 str pos: 0x617560 length: 1
.

key pos: 0x61e083 str pos: 0x61dd6b length: 12
kernel32.dll

key pos: 0x6212f1 str pos: 0x62104e length: 15
AddDllDirectory

key pos: 0x61755c str pos: 0x617563 length: 1
\

key pos: 0x61755f str pos: 0x617566 length: 1
-

key pos: 0x617559 str pos: 0x617559 length: 1


key pos: 0x61cf5b str pos: 0x61ca6f length: 12
kernel32.dll

key pos: 0x618b48 str pos: 0x618d18 length: 8
SetEvent

key pos: 0x624567 str pos: 0x624d7e length: 19
WaitForSingleObject

key pos: 0x61d6ff str pos: 0x61eddf length: 12
advapi32.dll

key pos: 0x62a699 str pos: 0x62a6d3 length: 29
RegisterServiceCtrlHandlerExW

key pos: 0x6196e4 str pos: 0x6199e1 length: 9
ole32.dll

key pos: 0x61d40b str pos: 0x61cf43 length: 12
CoInitialize

key pos: 0x62042f str pos: 0x6202b5 length: 14
CoInitializeEx

key pos: 0x6208f1 str pos: 0x62060b length: 14
CoUninitialize

key pos: 0x6225d0 str pos: 0x622450 length: 16
CoCreateInstance

key pos: 0x61f290 str pos: 0x61f3d5 length: 13
CoTaskMemFree

key pos: 0x621ada str pos: 0x620e50 length: 15
CLSIDFromProgID

key pos: 0x6217dd str pos: 0x6214e0 length: 15
CLSIDFromString

key pos: 0x6214d1 str pos: 0x621756 length: 15
StringFromCLSID

key pos: 0x61faa3 str pos: 0x61f346 length: 13
StringFromIID

key pos: 0x61fa14 str pos: 0x61f7a4 length: 13
IIDFromString

key pos: 0x61b1f3 str pos: 0x61c7bc length: 11
CoGetObject

key pos: 0x61e5db str pos: 0x61d8a3 length: 12
kernel32.dll

key pos: 0x62385e str pos: 0x623ac2 length: 18
GetUserDefaultLCID

key pos: 0x61f4bf str pos: 0x61f881 length: 13
RtlMoveMemory

key pos: 0x61ddef str pos: 0x61e0a7 length: 12
oleaut32.dll

key pos: 0x61bf03 str pos: 0x61c2f7 length: 11
VariantInit

key pos: 0x61e99b str pos: 0x61ccaf length: 12
VariantClear

key pos: 0x627692 str pos: 0x627595 length: 23
VariantTimeToSystemTime

key pos: 0x62058d str pos: 0x6207a1 length: 14
SysAllocString

key pos: 0x622ef7 str pos: 0x62306d length: 17
SysAllocStringLen

key pos: 0x61f2aa str pos: 0x61f3ae length: 13
SysFreeString

key pos: 0x61d4cb str pos: 0x61d1d7 length: 12
SysStringLen

key pos: 0x623a32 str pos: 0x623bac length: 18
CreateDispTypeInfo

key pos: 0x622e3c str pos: 0x6233f2 length: 17
CreateStdDispatch

key pos: 0x620ef5 str pos: 0x621c42 length: 15
GetActiveObject

key pos: 0x61a4a4 str pos: 0x61abc0 length: 10
user32.dll

key pos: 0x61b957 str pos: 0x61b5fd length: 11
GetMessageW

key pos: 0x621e10 str pos: 0x622730 length: 16
DispatchMessageW

key pos: 0x62d612 str pos: 0x62d508 length: 38
{00000000-0000-0000-0000-000000000000}

key pos: 0x62d6f6 str pos: 0x62d3d8 length: 38
{00000000-0000-0000-C000-000000000046}

key pos: 0x62d38c str pos: 0x62d71c length: 38
{00020400-0000-0000-C000-000000000046}

key pos: 0x62d4bc str pos: 0x62d638 length: 38
{00020404-0000-0000-C000-000000000046}

key pos: 0x62d6d0 str pos: 0x62d3fe length: 38
{B196B284-BAB4-101A-B69C-00AA00341D07}

key pos: 0x62d898 str pos: 0x62d3b2 length: 38
{B196B286-BAB4-101A-B69C-00AA00341D07}

key pos: 0x62d52e str pos: 0x62da3a length: 38
{AF86E2E0-B12D-4C6A-9C5A-D7AA65101E90}

key pos: 0x62d5ec str pos: 0x62d5a0 length: 38
{B196B283-BAB4-101A-B69C-00AA00341D07}

key pos: 0x62d424 str pos: 0x62d65e length: 38
{E0133EB4-C36F-469A-9D3D-C66B84BE19ED}

key pos: 0x62d4e2 str pos: 0x62da60 length: 38
{BEB06610-EB84-4155-AF58-E2BFF53680B4}

key pos: 0x62da86 str pos: 0x62d496 length: 38
{DAA3F9FA-761E-4976-A860-8364CE55F6FC}

key pos: 0x62d1ea str pos: 0x62d282 length: 38
{E3DEDEE7-38A2-4540-91D1-2EEF1D8891B0}

key pos: 0x62d1c4 str pos: 0x62d2a8 length: 38
{8D437CBC-B3ED-485C-BC32-C336432A1623}

key pos: 0x62d340 str pos: 0x62d7b4 length: 38
{BF1ED004-EA02-456A-AA55-2AC8AC6B054C}

key pos: 0x62d554 str pos: 0x62da14 length: 38
{BF908A81-8687-4E93-999F-D86FAB284BA0}

key pos: 0x62d6aa str pos: 0x62d44a length: 38
{D530E7A6-4EE8-40D1-8931-3D63B8605010}

key pos: 0x62d684 str pos: 0x62d470 length: 38
{6485B1EF-D780-4834-A4FE-1EBB51746CA3}

key pos: 0x62d210 str pos: 0x62d2ce length: 38
{CCA8D7AE-91C0-4277-A8B3-FF4EDF28D3C0}

key pos: 0x62d5c6 str pos: 0x62d57a length: 38
{3C24506A-AE9E-4D50-9157-EF317281F1B0}

key pos: 0x62d930 str pos: 0x62d31a length: 38
{865B85C5-0334-4AC6-9EF6-AACEC8FC5E86}

key pos: 0x621dc0 str pos: 0x6222a0 length: 16
0123456789ABCDEF

key pos: 0x62d78e str pos: 0x62d366 length: 38
{00000000-0000-0000-0000-000000000000}

key pos: 0x623fc3 str pos: 0x624d32 length: 19
SafeArrayAccessData

key pos: 0x623b0a str pos: 0x623882 length: 18
SafeArrayAllocData

key pos: 0x627eb6 str pos: 0x627f8e length: 24
SafeArrayAllocDescriptor

key pos: 0x628d77 str pos: 0x629619 length: 26
SafeArrayAllocDescriptorEx

key pos: 0x61f763 str pos: 0x61f8e9 length: 13
SafeArrayCopy

key pos: 0x622c1c str pos: 0x622db4 length: 17
SafeArrayCopyData

key pos: 0x621774 str pos: 0x62151c length: 15
SafeArrayCreate

key pos: 0x62305c str pos: 0x622f2a length: 17
SafeArrayCreateEx

key pos: 0x625af8 str pos: 0x62625a length: 21
SafeArrayCreateVector

key pos: 0x627242 str pos: 0x6274af length: 23
SafeArrayCreateVectorEx

key pos: 0x622330 str pos: 0x6224e0 length: 16
SafeArrayDestroy

key pos: 0x6259e8 str pos: 0x624e6c length: 20
SafeArrayDestroyData

key pos: 0x62964d str pos: 0x629187 length: 26
SafeArrayDestroyDescriptor

key pos: 0x62152b str pos: 0x621783 length: 15
SafeArrayGetDim

key pos: 0x6245c6 str pos: 0x6247a1 length: 19
SafeArrayGetElement

key pos: 0x625650 str pos: 0x6251c8 length: 20
SafeArrayGetElemsize

key pos: 0x6212d3 str pos: 0x62116b length: 15
SafeArrayGetIID

key pos: 0x623af8 str pos: 0x623870 length: 18
SafeArrayGetLBound

key pos: 0x623b40 str pos: 0x623894 length: 18
SafeArrayGetUBound

key pos: 0x62444a str pos: 0x62412c length: 19
SafeArrayGetVartype

key pos: 0x61f0e3 str pos: 0x61fbc1 length: 13
SafeArrayLock

key pos: 0x624872 str pos: 0x6246e3 length: 19
SafeArrayPtrOfIndex

key pos: 0x625ab9 str pos: 0x626539 length: 21
SafeArrayUnaccessData

key pos: 0x621855 str pos: 0x6214a4 length: 15
SafeArrayUnlock

key pos: 0x624684 str pos: 0x6248e4 length: 19
SafeArrayPutElement

key pos: 0x626af6 str pos: 0x6269ee length: 22
SafeArrayGetRecordInfo

key pos: 0x627060 str pos: 0x626980 length: 22
SafeArraySetRecordInfo

key pos: 0x61c0b0 str pos: 0x61bd4b length: 11
combase.dll

key pos: 0x630be0 str pos: 0x630c4e length: 110
VT_EMPTYVT_NULLVT_I2VT_I4VT_R4VT_R8VT_CYVT_DATEVT_BSTRVT_DISPATCHVT_ERRORVT_BOOLVT_VARIANTVT_UNKNOWNVT_DECIMAL

key pos: 0x630d36 str pos: 0x630cbc length: 122
VT_I1VT_UI1VT_UI2VT_UI4VT_I8VT_UI8VT_INTVT_UINTVT_VOIDVT_HRESULTVT_PTRVT_SAFEARRAYVT_CARRAYVT_USERDEFINEDVT_LPSTRVT_LPWSTR

key pos: 0x62aef1 str pos: 0x62af4b length: 30
VT_RECORDVT_INT_PTRVT_UINT_PTR

key pos: 0x630b14 str pos: 0x630ab2 length: 98
VT_FILETIMEVT_BLOBVT_STREAMVT_STORAGEVT_STREAMED_OBJECTVT_STORED_OBJECTVT_BLOB_OBJECTVT_CFVT_CLSID

key pos: 0x6260cb str pos: 0x625fcf length: 21
VT_BSTR_BLOBVT_VECTOR

key pos: 0x618f68 str pos: 0x618a40 length: 8
VT_ARRAY

key pos: 0x618bf0 str pos: 0x618ca0 length: 8
VT_BYREF

key pos: 0x61bff5 str pos: 0x61bb1a length: 11
VT_RESERVED

key pos: 0x61a742 str pos: 0x61ac10 length: 10
VT_ILLEGAL

key pos: 0x61d06f str pos: 0x61d477 length: 12
RoInitialize

key pos: 0x623804 str pos: 0x62361e length: 18
RoActivateInstance

key pos: 0x6266aa str pos: 0x626d48 length: 22
RoGetActivationFactory

key pos: 0x6245b3 str pos: 0x62477b length: 19
WindowsCreateString

key pos: 0x624930 str pos: 0x624612 length: 19
WindowsDeleteString

key pos: 0x6284ab str pos: 0x62863b length: 25
WindowsGetStringRawBuffer

key pos: 0x61755a str pos: 0x61755a length: 1


key pos: 0x6175af str pos: 0x617637 length: 2
 (

key pos: 0x617562 str pos: 0x61755e length: 1
)

key pos: 0x62dddf str pos: 0x62de7f length: 40
error %d (FormatMessage failed with: %v)

key pos: 0x6243fe str pos: 0x6240ba length: 19
2006-01-02 15:04:05

key pos: 0x624c74 str pos: 0x62413f length: 19
2006-01-02 15:04:05

key pos: 0x61e74f str pos: 0x61d7e3 length: 12
unknown type

key pos: 0x617ec2 str pos: 0x617e77 length: 5
<nil>

key pos: 0x617f85 str pos: 0x617d1e length: 5
<nil>

key pos: 0x617c6f str pos: 0x617dcd length: 5
<nil>

key pos: 0x630a51 str pos: 0x6309f0 length: 97
wCode: %#x, bstrSource: %v, bstrDescription: %v, bstrHelpFile: %v, dwHelpContext: %#x, scode: %#x

key pos: 0x618722 str pos: 0x6187e6 length: 7
Unknown

key pos: 0x6183a9 str pos: 0x61862d length: 7
%v: %#x

key pos: 0x62ce27 str pos: 0x62ce4c length: 37
Could not convert []byte to SAFEARRAY

key pos: 0x62db96 str pos: 0x62db21 length: 39
Could not convert []string to SAFEARRAY

key pos: 0x62f157 str pos: 0x62f127 length: 48
Could not convert to time, passing current time.

key pos: 0x61807a str pos: 0x61818e length: 6
VT(%d)

key pos: 0x627c76 str pos: 0x627b9e length: 24
wmi: invalid entity type

key pos: 0x62b3c7 str pos: 0x62b424 length: 31
wmi: create object returned nil

key pos: 0x62b7a7 str pos: 0x62bb07 length: 32
SWbemServices is not Initialized

key pos: 0x62a812 str pos: 0x62a747 length: 29
SWbemServices has been closed

key pos: 0x62b867 str pos: 0x62b8c7 length: 32
SWbemServices is not Initialized

key pos: 0x62a82f str pos: 0x62a764 length: 29
SWbemServices has been closed

key pos: 0x629083 str pos: 0x628f4b length: 26
WbemScripting.SWbemLocator

key pos: 0x61f59c str pos: 0x61f840 length: 13
ConnectServer

key pos: 0x61920a str pos: 0x619bd9 length: 9
ExecQuery

key pos: 0x617e81 str pos: 0x617df0 length: 5
Count

key pos: 0x618db8 str pos: 0x618e58 length: 8
_NewEnum

key pos: 0x62c756 str pos: 0x62c733 length: 35
can't get IEnumVARIANT, enum is nil

key pos: 0x62db48 str pos: 0x62db6f length: 39
wmi: cannot load field %q into a %q: %s

key pos: 0x622c3e str pos: 0x622d5f length: 17
CanSet() is false

key pos: 0x625448 str pos: 0x6253d0 length: 20
no such struct field

key pos: 0x625344 str pos: 0x6255d8 length: 20
not an integer class

key pos: 0x625290 str pos: 0x625574 length: 20
not an integer class

key pos: 0x618d68 str pos: 0x618e10 length: 8
%02d%02d

key pos: 0x629069 str pos: 0x628df9 length: 26
20060102150405.000000-0700

key pos: 0x61aed6 str pos: 0x61a3e6 length: 10
not a bool

key pos: 0x61f21b str pos: 0x61ef02 length: 13
not a Float32

key pos: 0x629867 str pos: 0x6299c6 length: 27
unsupported slice type (%T)

key pos: 0x626578 str pos: 0x62600e length: 21
unsupported type (%T)

key pos: 0x622cf9 str pos: 0x622a95 length: 17
command timed out

key pos: 0x623f8a str pos: 0x6242e1 length: 19
not implemented yet

key pos: 0x61d1bf str pos: 0x61cdb7 length: 12
kernel32.dll

key pos: 0x619507 str pos: 0x619add length: 9
ntdll.dll

key pos: 0x6184f9 str pos: 0x618458 length: 7
pdh.dll

key pos: 0x61983a str pos: 0x6198af length: 9
psapi.dll

key pos: 0x6203b1 str pos: 0x6200af length: 14
GetSystemTimes

key pos: 0x627c8e str pos: 0x627dde length: 24
NtQuerySystemInformation

key pos: 0x61e887 str pos: 0x61d5af length: 12
PdhOpenQuery

key pos: 0x6203e9 str pos: 0x620a5d length: 14
PdhAddCounterW

key pos: 0x624b31 str pos: 0x624119 length: 19
PdhCollectQueryData

key pos: 0x629831 str pos: 0x6297aa length: 27
PdhGetFormattedCounterValue

key pos: 0x61f8c2 str pos: 0x61f73c length: 13
PdhCloseQuery

key pos: 0x6216a2 str pos: 0x621909 length: 15
QueryDosDeviceW

key pos: 0x62457a str pos: 0x624d91 length: 19
GetDiskFreeSpaceExW

key pos: 0x6275ac str pos: 0x62764d length: 23
GetLogicalDriveStringsW

key pos: 0x61f7d8 str pos: 0x61f50d length: 13
GetDriveTypeW

key pos: 0x625ff9 str pos: 0x62619d length: 21
GetVolumeInformationW

key pos: 0x617535 str pos: 0x617558 length: 1
:

key pos: 0x617643 str pos: 0x6175b1 length: 2
:/

key pos: 0x617623 str pos: 0x617633 length: 2
rw

key pos: 0x6175f1 str pos: 0x617587 length: 2
ro

key pos: 0x619249 str pos: 0x6195cd length: 9
.compress

key pos: 0x61754f str pos: 0x61754f length: 1


key pos: 0x62d2f4 str pos: 0x62d8e4 length: 38
expected a single entry rather than %d

key pos: 0x62febe str pos: 0x62fef7 length: 57
cannot walk without non-nil options and Callback function

key pos: 0x62a53d str pos: 0x62a594 length: 29
cannot Walk non-directory: %s

key pos: 0x62995a str pos: 0x629924 length: 27
osChildname: %q; error: %v


key pos: 0x61e77f str pos: 0x61da8f length: 12
kernel32.dll

key pos: 0x61b209 str pos: 0x61c861 length: 11
CloseHandle

key pos: 0x627f46 str pos: 0x62804e length: 24
CreateToolhelp32Snapshot

key pos: 0x621cab str pos: 0x620e6e length: 15
Process32FirstW

key pos: 0x620a4f str pos: 0x6203bf length: 14
Process32NextW

key pos: 0x62aeb5 str pos: 0x62af0f length: 30
Error retrieving process info.

key pos: 0x61d9f3 str pos: 0x61e4f7 length: 12
kernel32.dll

key pos: 0x61ca63 str pos: 0x61e8cf length: 12
CreateMutexW

key pos: 0x626c56 str pos: 0x62693e length: 22
Decrypt-Your-Files.txt

key pos: 0x62f843 str pos: 0x62f7db length: 52
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

key pos: 0x617f12 str pos: 0x617d8c length: 5
EKANS

key pos: 0x62a06d str pos: 0x62a0c1 length: 28
could not access service: %v

key pos: 0x62a84c str pos: 0x62a70d length: 29
could not send control=%d: %v

key pos: 0x62e9c4 str pos: 0x62e9f1 length: 45
timeout waiting for service to go to state=%d

key pos: 0x62ce02 str pos: 0x62cebb length: 37
could not retrieve service status: %v

key pos: 0x625664 str pos: 0x624da4 length: 20
Acronis VSS Provider

key pos: 0x62882f str pos: 0x6286ea length: 25
Enterprise Client Service

key pos: 0x61d43b str pos: 0x61d15f length: 12
Sophos Agent

key pos: 0x628d2a str pos: 0x628703 length: 25
Sophos AutoUpdate Service

key pos: 0x6254ac str pos: 0x625380 length: 20
Sophos Clean Service

key pos: 0x62a869 str pos: 0x62a7bb length: 29
Sophos Device Control Service

key pos: 0x629a9e str pos: 0x629708 length: 27
Sophos File Scanner Service

key pos: 0x625ed3 str pos: 0x62604d length: 21
Sophos Health Service

key pos: 0x6220a0 str pos: 0x6221e0 length: 16
Sophos MCS Agent

key pos: 0x622e2b str pos: 0x6233d0 length: 17
Sophos MCS Client

key pos: 0x625ebe str pos: 0x626563 length: 21
Sophos Message Router

key pos: 0x627e26 str pos: 0x627be6 length: 24
Sophos Safestore Service

key pos: 0x62b8a7 str pos: 0x62b887 length: 32
Sophos System Protection Service

key pos: 0x629257 str pos: 0x62916d length: 26
Sophos Web Control Service

key pos: 0x626862 str pos: 0x6268ba length: 22
SQLsafe Backup Service

key pos: 0x626ab4 str pos: 0x626bd2 length: 22
SQLsafe Filter Service

key pos: 0x627ece str pos: 0x627f76 length: 24
Symantec System Recovery

key pos: 0x62be6c str pos: 0x62becf length: 33
Veeam Backup Catalog Data Service

key pos: 0x61cd0f str pos: 0x61ed4f length: 12
AcronisAgent

key pos: 0x61a512 str pos: 0x61a92c length: 10
AcrSch2Svc

key pos: 0x6194fe str pos: 0x6196b7 length: 9
Antivirus

key pos: 0x617b08 str pos: 0x61789c length: 4
ARSM

key pos: 0x629633 str pos: 0x6290d1 length: 26
BackupExecAgentAccelerator

key pos: 0x626fdc str pos: 0x626668 length: 22
BackupExecAgentBrowser

key pos: 0x62a0f9 str pos: 0x62a0a5 length: 28
BackupExecDeviceMediaService

key pos: 0x6243eb str pos: 0x6241ea length: 19
BackupExecJobEngine

key pos: 0x6297fb str pos: 0x629816 length: 27
BackupExecManagementService

key pos: 0x6251b4 str pos: 0x624f48 length: 20
BackupExecRPCService

key pos: 0x625a7a str pos: 0x626284 length: 21
BackupExecVSSProvider

key pos: 0x617e95 str pos: 0x617e54 length: 5
bedbg

key pos: 0x61844a str pos: 0x61892f length: 7
DCAgent

key pos: 0x622ed5 str pos: 0x622f90 length: 17
EPSecurityService

key pos: 0x6215df str pos: 0x621882 length: 15
EPUpdateService

key pos: 0x620d5f str pos: 0x62005b length: 14
EraserSvc11710

key pos: 0x61b7e1 str pos: 0x61b311 length: 11
EsgShKernel

key pos: 0x61e1bb str pos: 0x61d9db length: 12
FA_Scheduler

key pos: 0x618e28 str pos: 0x618f30 length: 8
IISAdmin

key pos: 0x618a60 str pos: 0x619048 length: 8
IMAP4Svc

key pos: 0x618f50 str pos: 0x618d70 length: 8
macmnsvc

key pos: 0x617d5a str pos: 0x617cec length: 5
masvc

key pos: 0x61c016 str pos: 0x61ba3e length: 11
MBAMService

key pos: 0x621477 str pos: 0x621cf6 length: 15
MBEndpointAgent

key pos: 0x624742 str pos: 0x624508 length: 19
McAfeeEngineService

key pos: 0x621369 str pos: 0x62122e length: 15
McAfeeFramework

key pos: 0x62ae79 str pos: 0x62ae3d length: 30
McAfeeFrameworkMcAfeeFramework

key pos: 0x618e20 str pos: 0x618f40 length: 8
McShield

key pos: 0x61fa21 str pos: 0x61f77d length: 13
McTaskManager

key pos: 0x618170 str pos: 0x61825a length: 6
mfemms

key pos: 0x6180c8 str pos: 0x617ff6 length: 6
mfevtp

key pos: 0x61f7be str pos: 0x61f88e length: 13
mozyprobackup

key pos: 0x61c113 str pos: 0x61bbe0 length: 11
MsDtsServer

key pos: 0x61fe47 str pos: 0x620b9f length: 14
MsDtsServer100

key pos: 0x620563 str pos: 0x620da5 length: 14
MsDtsServer110

key pos: 0x61ed1f str pos: 0x61cd4b length: 12
MSExchangeES

key pos: 0x61cbbf str pos: 0x61e8b7 length: 12
MSExchangeIS

key pos: 0x620a6b str pos: 0x61ff19 length: 14
MSExchangeMGMT

key pos: 0x61fd13 str pos: 0x61f06e length: 13
MSExchangeMTA

key pos: 0x61e8e7 str pos: 0x61cba7 length: 12
MSExchangeSA

key pos: 0x61f5ea str pos: 0x61f89b length: 13
MSExchangeSRS

key pos: 0x62153a str pos: 0x621d23 length: 15
MSOLAP$SQL_2008

key pos: 0x622a62 str pos: 0x6233bf length: 17
MSOLAP$SYSTEM_BGC

key pos: 0x61a97c str pos: 0x61a4cc length: 10
MSOLAP$TPS

key pos: 0x61f715 str pos: 0x61f8dc length: 13
MSOLAP$TPSAMA

key pos: 0x620619 str pos: 0x620849 length: 14
MSSQL$BKUPEXEC

key pos: 0x61d48f str pos: 0x61d04b length: 12
MSSQL$ECWDB2

key pos: 0x6230b1 str pos: 0x6229da length: 17
MSSQL$PRACTICEMGT

key pos: 0x623b76 str pos: 0x6239fc length: 18
MSSQL$PRACTTICEBGC

key pos: 0x6260a1 str pos: 0x625f12 length: 21
MSSQL$PROFXENGAGEMENT

key pos: 0x624826 str pos: 0x62452e length: 19
MSSQL$SBSMONITORING

key pos: 0x621f20 str pos: 0x6221d0 length: 16
MSSQL$SHAREPOINT

key pos: 0x620a09 str pos: 0x62074d length: 14
MSSQL$SQL_2008

key pos: 0x622430 str pos: 0x622640 length: 16
MSSQL$SYSTEM_BGC

key pos: 0x6194e3 str pos: 0x6192f4 length: 9
MSSQL$TPS

key pos: 0x61e1a3 str pos: 0x61d84f length: 12
MSSQL$TPSAMA

key pos: 0x625768 str pos: 0x624e1c length: 20
MSSQL$VEEAMSQL2008R2

key pos: 0x623480 str pos: 0x623c72 length: 18
MSSQL$VEEAMSQL2012

key pos: 0x62171a str pos: 0x621981 length: 15
MSSQLFDLauncher

key pos: 0x62b3a8 str pos: 0x62b405 length: 31
MSSQLFDLauncher$PROFXENGAGEMENT

key pos: 0x62a72a str pos: 0x62a7f5 length: 29
MSSQLFDLauncher$SBSMONITORING

key pos: 0x62923d str pos: 0x6290eb length: 26
MSSQLFDLauncher$SHAREPOINT

key pos: 0x627f5e str pos: 0x627e56 length: 24
MSSQLFDLauncher$SQL_2008

key pos: 0x629327 str pos: 0x629223 length: 26
MSSQLFDLauncher$SYSTEM_BGC

key pos: 0x62431a str pos: 0x6244a9 length: 19
MSSQLFDLauncher$TPS

key pos: 0x6268fc str pos: 0x626878 length: 22
MSSQLFDLauncher$TPSAMA

key pos: 0x61c420 str pos: 0x61bec1 length: 11
MSSQLSERVER

key pos: 0x62688e str pos: 0x626928 length: 22
MSSQLServerADHelper100

key pos: 0x62667e str pos: 0x627034 length: 22
MSSQLServerOLAPService

key pos: 0x6187bc str pos: 0x6186f1 length: 7
MySQL57

key pos: 0x618d58 str pos: 0x618ee8 length: 8
ntrtscan

key pos: 0x624d45 str pos: 0x624048 length: 19
OracleClientCache80

key pos: 0x61e053 str pos: 0x61e63b length: 12
PDVFSService

key pos: 0x618887 str pos: 0x61842e length: 7
POP3Svc

key pos: 0x61d693 str pos: 0x61cf97 length: 12
ReportServer

key pos: 0x625fe4 str pos: 0x62610a length: 21
ReportServer$SQL_2008

key pos: 0x627567 str pos: 0x627b10 length: 23
ReportServer$SYSTEM_BGC

key pos: 0x6221b0 str pos: 0x621e00 length: 16
ReportServer$TPS

key pos: 0x624b44 str pos: 0x6240e0 length: 19
ReportServer$TPSAMA

key pos: 0x617eae str pos: 0x617e3b length: 5
RESvc

key pos: 0x618176 str pos: 0x6182f0 length: 6
sacsvr

key pos: 0x617e36 str pos: 0x617eb3 length: 5
SamSs

key pos: 0x621666 str pos: 0x621873 length: 15
SAVAdminService

key pos: 0x61a116 str pos: 0x61a454 length: 10
SAVService

key pos: 0x618200 str pos: 0x6181c4 length: 6
SDRSVC

key pos: 0x622520 str pos: 0x6222c0 length: 16
SepMasterService

key pos: 0x6193e7 str pos: 0x6194da length: 9
ShMonitor

key pos: 0x618420 str pos: 0x618833 length: 7
Smcinst

key pos: 0x61ad32 str pos: 0x619f36 length: 10
SmcService

key pos: 0x618394 str pos: 0x618921 length: 7
SMTPSvc

key pos: 0x617aac str pos: 0x617a30 length: 4
SNAC

key pos: 0x61bce8 str pos: 0x61c40a length: 11
SntpService

key pos: 0x61957c str pos: 0x619a68 length: 9
sophossps

key pos: 0x622ab7 str pos: 0x62318e length: 17
SQLAgent$BKUPEXEC

key pos: 0x6219cc str pos: 0x62162a length: 15
SQLAgent$ECWDB2

key pos: 0x6261b2 str pos: 0x625f90 length: 21
SQLAgent$PRACTTICEBGC

key pos: 0x626524 str pos: 0x625a50 length: 21
SQLAgent$PRACTTICEMGT

key pos: 0x627df6 str pos: 0x627dc6 length: 24
SQLAgent$PROFXENGAGEMENT

key pos: 0x6265b8 str pos: 0x62701e length: 22
SQLAgent$SBSMONITORING

key pos: 0x624541 str pos: 0x624755 length: 19
SQLAgent$SHAREPOINT

key pos: 0x622974 str pos: 0x623304 length: 17
SQLAgent$SQL_2008

key pos: 0x624956 str pos: 0x62406e length: 19
SQLAgent$SYSTEM_BGC

key pos: 0x61de73 str pos: 0x61e44f length: 12
SQLAgent$TPS

key pos: 0x621684 str pos: 0x6218fa length: 15
SQLAgent$TPSAMA

key pos: 0x627259 str pos: 0x6274c6 length: 23
SQLAgent$VEEAMSQL2008R2

key pos: 0x626077 str pos: 0x625f27 length: 21
SQLAgent$VEEAMSQL2012

key pos: 0x61a6f2 str pos: 0x61aba2 length: 10
SQLBrowser

key pos: 0x622b3f str pos: 0x622d81 length: 17
SQLSafeOLRService

key pos: 0x62096f str pos: 0x62073f length: 14
SQLSERVERAGENT

key pos: 0x61e1af str pos: 0x61db8b length: 12
SQLTELEMETRY

key pos: 0x62484c str pos: 0x6246aa length: 19
SQLTELEMETRY$ECWDB2

key pos: 0x61980d str pos: 0x6199a2 length: 9
SQLWriter

key pos: 0x61878b str pos: 0x6186a4 length: 7
SstpSvc

key pos: 0x620b83 str pos: 0x620467 length: 14
svcGenericHost

key pos: 0x61a904 str pos: 0x61a7e2 length: 10
swi_filter

key pos: 0x61b235 str pos: 0x61b43a length: 11
swi_service

key pos: 0x61fab0 str pos: 0x61f006 length: 13
swi_update_64

key pos: 0x618230 str pos: 0x6181e2 length: 6
TmCCSF

key pos: 0x619020 str pos: 0x618d30 length: 8
tmlisten

key pos: 0x61837f str pos: 0x618928 length: 7
TrueKey

key pos: 0x622090 str pos: 0x622240 length: 16
TrueKeyScheduler

key pos: 0x625498 str pos: 0x625358 length: 20
TrueKeyServiceHelper

key pos: 0x6196c9 str pos: 0x61989d length: 9
UI0Detect

key pos: 0x620387 str pos: 0x61fee1 length: 14
VeeamBackupSvc

key pos: 0x6208e3 str pos: 0x6204f3 length: 14
VeeamBrokerSvc

key pos: 0x62160c str pos: 0x621a26 length: 15
VeeamCatalogSvc

key pos: 0x61f1a6 str pos: 0x61f498 length: 13
VeeamCloudSvc

key pos: 0x626b0c str pos: 0x6269d8 length: 22
VeeamDeploymentService

key pos: 0x61fe7f str pos: 0x620c39 length: 14
VeeamDeploySvc

key pos: 0x628735 str pos: 0x6287fd length: 25
VeeamEnterpriseManagerSvc

key pos: 0x61f201 str pos: 0x61f464 length: 13
VeeamMountSvc

key pos: 0x61c722 str pos: 0x61b10c length: 11
VeeamNFSSvc

key pos: 0x61dabf str pos: 0x61ee0f length: 12
VeeamRESTSvc

key pos: 0x622d92 str pos: 0x622bd8 length: 17
VeeamTransportSvc

key pos: 0x617eb8 str pos: 0x617e2c length: 5
W3Svc

key pos: 0x619008 str pos: 0x618d28 length: 8
wbengine

key pos: 0x617fa3 str pos: 0x617ddc length: 5
WRSVC

key pos: 0x625dc2 str pos: 0x6261c7 length: 21
VeeamHvIntegrationSvc

key pos: 0x61a0a8 str pos: 0x619f0e length: 10
swi_update

key pos: 0x61fcab str pos: 0x61ef9e length: 13
SQLAgent$CXDB

key pos: 0x628686 str pos: 0x628528 length: 25
SQLAgent$CITRIX_METAFRAME

key pos: 0x61b68c str pos: 0x61b61e length: 11
SQL Backups

key pos: 0x61a5bc str pos: 0x61a8fa length: 10
MSSQL$PROD

key pos: 0x621ce7 str pos: 0x620e5f length: 15
Zoolz 2 Service

key pos: 0x6248ab str pos: 0x624709 length: 19
MSSQLServerADHelper

key pos: 0x61f07b str pos: 0x61fb4c length: 13
SQLAgent$PROD

key pos: 0x61fda2 str pos: 0x61f797 length: 13
msftesql$PROD

key pos: 0x622000 str pos: 0x622210 length: 16
NetMsmqActivator

key pos: 0x618cb8 str pos: 0x618b58 length: 8
EhttpSrv

key pos: 0x617a68 str pos: 0x617a38 length: 4
ekrn

key pos: 0x6185e0 str pos: 0x61866c length: 7
ESHASRV

key pos: 0x61cb47 str pos: 0x61ea43 length: 12
MSSQL$SOPHOS

key pos: 0x6218cd str pos: 0x621648 length: 15
SQLAgent$SOPHOS

key pos: 0x618a48 str pos: 0x618f58 length: 8
klnagent

key pos: 0x622170 str pos: 0x622250 length: 16
MSSQL$SQLEXPRESS

key pos: 0x6246bd str pos: 0x624885 length: 19
SQLAgent$SQLEXPRESS

key pos: 0x6190d0 str pos: 0x618e00 length: 8
kavfsslp

key pos: 0x618802 str pos: 0x618737 length: 7
KAVFSGT

key pos: 0x617e40 str pos: 0x617ea4 length: 5
KAVFS

key pos: 0x61868f str pos: 0x6187b5 length: 7
mfefire

key pos: 0x622140 str pos: 0x621e80 length: 16
avast! Antivirus

key pos: 0x6182ea str pos: 0x61819a length: 6
aswBcc

key pos: 0x62eeef str pos: 0x62ef1e length: 47
Avast Business Console Client Antivirus Service

key pos: 0x617d41 str pos: 0x617c60 length: 5
mfewc

key pos: 0x621a9e str pos: 0x620f13 length: 15
Telemetryserver

key pos: 0x618d00 str pos: 0x618aa8 length: 8
WdNisSvc

key pos: 0x6198ee str pos: 0x619627 length: 9
WinDefend

key pos: 0x623d4a str pos: 0x62345c length: 18
MCAFEETOMCATSRV530

key pos: 0x625434 str pos: 0x625588 length: 20
MCAFEEEVENTPARSERSRV

key pos: 0x625f7b str pos: 0x62658d length: 21
MSSQLFDLauncher$ITRIS

key pos: 0x621bd9 str pos: 0x620f6d length: 15
MSSQL$EPOSERVER

key pos: 0x61b52c str pos: 0x61b94c length: 11
MSSQL$ITRIS

key pos: 0x623a9e str pos: 0x623936 length: 18
SQLAgent$EPOSERVER

key pos: 0x6207e7 str pos: 0x6205fd length: 14
SQLAgent$ITRIS

key pos: 0x623948 str pos: 0x623ae6 length: 18
SQLTELEMETRY$ITRIS

key pos: 0x62019d str pos: 0x62036b length: 14
MsDtsServer130

key pos: 0x622350 str pos: 0x6224d0 length: 16
SSISTELEMETRY130

key pos: 0x62522c str pos: 0x625074 length: 20
MSSQLLaunchpad$ITRIS

key pos: 0x6178c4 str pos: 0x617b30 length: 4
BITS

key pos: 0x625204 str pos: 0x625150 length: 20
BrokerInfrastructure

key pos: 0x6179e0 str pos: 0x617b90 length: 4
epag

key pos: 0x62531c str pos: 0x62554c length: 20
EPIntegrationService

key pos: 0x6238dc str pos: 0x623a7a length: 18
EPProtectedService

key pos: 0x6191b9 str pos: 0x61937b length: 9
epredline

key pos: 0x617e86 str pos: 0x617e22 length: 5
TmPfw

key pos: 0x61f471 str pos: 0x61f1c0 length: 13
SentinelAgent

key pos: 0x626062 str pos: 0x625ee8 length: 21
SentinelHelperService

key pos: 0x623ffc str pos: 0x62497c length: 19
LogProcessorService

key pos: 0x6259c0 str pos: 0x624e44 length: 20
SentinelStaticEngine

key pos: 0x62540c str pos: 0x62559c length: 20
DB2GOVERNOR_DB2COPY1

key pos: 0x6222d0 str pos: 0x6224f0 length: 16
DB2LICD_DB2COPY1

key pos: 0x6245a0 str pos: 0x624839 length: 19
DB2MGMTSVC_DB2COPY1

key pos: 0x625d59 str pos: 0x625e40 length: 21
DB2REMOTECMD_DB2COPY1

key pos: 0x618cd0 str pos: 0x618ba8 length: 8
DB2DAS00

key pos: 0x617f76 str pos: 0x617cc4 length: 5
DB2-0

key pos: 0x618ef0 str pos: 0x618dc0 length: 8
DB2INST2

key pos: 0x622180 str pos: 0x622050 length: 16
IBMDataServerMgr

key pos: 0x61fa96 str pos: 0x61f430 length: 13
IBMDSServer41

key pos: 0x626996 str pos: 0x626ae0 length: 22
MSSQL$CITRIX_METAFRAME

key pos: 0x61bd2a str pos: 0x61c499 length: 11
RumorServer

key pos: 0x618f00 str pos: 0x618d40 length: 8
myAgtSvc

key pos: 0x62ce96 str pos: 0x62ce71 length: 37
McAfee SiteAdvisor Enterprise Service

key pos: 0x61889c str pos: 0x6183b0 length: 7
Alerter

key pos: 0x617dbe str pos: 0x617d7d length: 5
ERSvc

key pos: 0x618d78 str pos: 0x618e80 length: 8
Eventlog

key pos: 0x61e66b str pos: 0x61df4b length: 12
ImapiService

key pos: 0x61828a str pos: 0x61802c length: 6
NetDDE

key pos: 0x6188f0 str pos: 0x618443 length: 7
NtLmSsp

key pos: 0x6186ab str pos: 0x618753 length: 7
NtmsSvc

key pos: 0x61821e str pos: 0x6181b8 length: 6
odserv

key pos: 0x624697 str pos: 0x62485f length: 19
SnowInventoryClient

key pos: 0x618611 str pos: 0x6185b6 length: 7
TlntSvr

key pos: 0x6186dc str pos: 0x618776 length: 7
VMTools

key pos: 0x6180b6 str pos: 0x618194 length: 6
VMware

key pos: 0x619987 str pos: 0x6197ce length: 9
WebClient

key pos: 0x61873e str pos: 0x6187a0 length: 7
WinVNC4

key pos: 0x6247b4 str pos: 0x6244e2 length: 19
BlueStripeCollector

key pos: 0x618f20 str pos: 0x618e08 length: 8
Cissesrv

key pos: 0x618cb0 str pos: 0x618b80 length: 8
CpqRcmc3

key pos: 0x618841 str pos: 0x61861f length: 7
gupdate

key pos: 0x618f18 str pos: 0x618d60 length: 8
gupdatem

key pos: 0x61f02d str pos: 0x61fcf9 length: 13
HealthService

key pos: 0x6256b4 str pos: 0x624e58 length: 20
NimbusWatcherService

key pos: 0x62117a str pos: 0x6212b5 length: 15
ProLiantMonitor

key pos: 0x61b89c str pos: 0x61b3c1 length: 11
SDD_Service

key pos: 0x618810 str pos: 0x6183d3 length: 7
sysdown

key pos: 0x61816a str pos: 0x618236 length: 6
System

key pos: 0x629e05 str pos: 0x62a521 length: 28
GoogleChromeElevationService

key pos: 0x61a8e6 str pos: 0x61a6ac length: 10
bcrservice

key pos: 0x619038 str pos: 0x618cc8 length: 8
ccEvtMgr

key pos: 0x618ad8 str pos: 0x618960 length: 8
ccSetMgr

key pos: 0x6187d8 str pos: 0x618745 length: 7
CSAdmin

key pos: 0x6181a6 str pos: 0x6182f6 length: 6
CSAuth

key pos: 0x619018 str pos: 0x6189f8 length: 8
CSDbSync

key pos: 0x617e72 str pos: 0x617de1 length: 5
CSLog

key pos: 0x617dfa str pos: 0x617e8b length: 5
CSMon

key pos: 0x618a50 str pos: 0x619080 length: 8
CSRadius

key pos: 0x618da0 str pos: 0x618ed8 length: 8
CSTacacs

key pos: 0x618e98 str pos: 0x618d48 length: 8
Symantec

key pos: 0x61f7b1 str pos: 0x61f951 length: 13
VGAuthService

key pos: 0x6244bc str pos: 0x624813 length: 19
SepMasterServiceMig

key pos: 0x62675a str pos: 0x62663c length: 22
vmware-converter-agent

key pos: 0x627425 str pos: 0x6270bb length: 23
vmware-converter-server

key pos: 0x627550 str pos: 0x62761f length: 23
vmware-converter-worker

key pos: 0x618e18 str pos: 0x618ea0 length: 8
avbackup

key pos: 0x61a63e str pos: 0x61aa3a length: 10
MSSQL$NET2

key pos: 0x61f360 str pos: 0x61f575 length: 13
Net2ClientSvc

key pos: 0x6181a0 str pos: 0x6181fa length: 6
NetSvc

key pos: 0x61f9e0 str pos: 0x61f686 length: 13
SQLAgent$NET2

key pos: 0x61f62b str pos: 0x61f9ac length: 13
tpautoconnsvc

key pos: 0x61b12d str pos: 0x61c809 length: 11
TPVCGateway

key pos: 0x628816 str pos: 0x62871c length: 25
VMwareCAFCommAmqpListener

key pos: 0x629e21 str pos: 0x62a361 length: 28
VMwareCAFManagementAgentHost

key pos: 0x621a53 str pos: 0x6213b4 length: 15
AdobeARMservice

key pos: 0x618363 str pos: 0x6188e9 length: 7
RSCDsvc

key pos: 0x61894b str pos: 0x6186c7 length: 7
LRSDRVX

key pos: 0x619372 str pos: 0x619171 length: 9
msvsmon90

key pos: 0x618a70 str pos: 0x619088 length: 8
IDriverT

key pos: 0x6179cc str pos: 0x61794c length: 4
MSMQ

key pos: 0x617838 str pos: 0x617679 length: 3
MMS

key pos: 0x62b3e6 str pos: 0x62b443 length: 31
MSSQLFDLauncher$PROFXENGAGEMENT

key pos: 0x6223a0 str pos: 0x622510 length: 16
ReportServer$TPS

key pos: 0x61a88c str pos: 0x61aaf8 length: 10
SQLBrowser

key pos: 0x6246f6 str pos: 0x6248d1 length: 19
MSSQLServerADHelper

key pos: 0x61f305 str pos: 0x61f32c length: 13
SQLAgent$PROD

key pos: 0x61fd06 str pos: 0x61f423 length: 13
msftesql$PROD

key pos: 0x621201 str pos: 0x6212e2 length: 15
SQLAgent$SOPHOS

key pos: 0x617763 str pos: 0x6177c6 length: 3
AVP

key pos: 0x6286b8 str pos: 0x628d11 length: 25
VeeamEnterpriseManagerSvc

key pos: 0x618817 str pos: 0x618634 length: 7
MySQL80

key pos: 0x62384c str pos: 0x623f54 length: 18
MSSQL$ARCSERVE_APP

key pos: 0x61fd61 str pos: 0x61f541 length: 13
ArcserveUDPPS

key pos: 0x61b705 str pos: 0x61b4b3 length: 11
CAARCAppSvc

key pos: 0x621396 str pos: 0x62121f length: 15
CASDatastoreSvc

key pos: 0x61f8a8 str pos: 0x61f652 length: 13
CASARPSWebSVC

key pos: 0x6208c7 str pos: 0x6205e1 length: 14
CAARCUpdateSvc

key pos: 0x61f55b str pos: 0x61fd7b length: 13
ArcserveUDPPS

key pos: 0x61fb18 str pos: 0x61efc5 length: 13
CASAD2DwebSvc

key pos: 0x61a6c0 str pos: 0x61aab2 length: 10
ASLogWatch

key pos: 0x626a88 str pos: 0x626c14 length: 22
FireEye Endpoint Agent

key pos: 0x617cd8 str pos: 0x617d87 length: 5
nxlog

key pos: 0x621792 str pos: 0x621558 length: 15
SplunkForwarder

key pos: 0x617856 str pos: 0x6176d0 length: 3
SAP

key pos: 0x617cdd str pos: 0x617f71 length: 5
MSSQL

key pos: 0x617f99 str pos: 0x617cbf length: 5
MySQL

key pos: 0x61f124 str pos: 0x61f353 length: 13
OracleService

key pos: 0x61f2f8 str pos: 0x61f0af length: 13
oracleservice

key pos: 0x617f9e str pos: 0x617dc8 length: 5
mssql

key pos: 0x618218 str pos: 0x6181dc length: 6
Sophos

key pos: 0x617e7c str pos: 0x617e13 length: 5
Veeam

key pos: 0x6185cb str pos: 0x61865e length: 7
Cylance

key pos: 0x6176eb str pos: 0x6177d8 length: 3
%v


key pos: 0x6177e1 str pos: 0x6177ed length: 3
%v


key pos: 0x617760 str pos: 0x61782f length: 3
%v


key pos: 0x6177d5 str pos: 0x6176ee length: 3
%v


key pos: 0x617841 str pos: 0x617742 length: 3
%v


key pos: 0x61780e str pos: 0x617805 length: 3
%v


key pos: 0x631759 str pos: 0x6311cc length: 1421
--------------------------------------------

| What happened to your files? 

--------------------------------------------

We breached your corporate network and encrypted the data on your computers. The encrypted data includes documents, databases, photos and more -

all were encrypted using a military grade encryption algorithms (AES-256 and RSA-2048). You cannot access those files right now. But dont worry!

You can still get those files back and be up and running again in no time. 


---------------------------------------------

| How to contact us to get your files back?

---------------------------------------------

The only way to restore your files is by purchasing a decryption tool loaded with a private key we created specifically for your network. 

Once run on an effected computer, the tool will decrypt all encrypted files - and you can resume day-to-day operations, preferably with

better cyber security in mind. If you are interested in purchasing the decryption tool contact us at %s


-------------------------------------------------------

| How can you be certain we have the decryption tool?

-------------------------------------------------------

In your mail to us attach up to 3 non critical files (up to 3MB, no databases or spreadsheets).

We will send them back to you decrypted. 

-------------------------------------------------------



key pos: 0x618188 str pos: 0x6182cc length: 6
public

key pos: 0x61c339 str pos: 0x61b98e length: 11
systemdrive

key pos: 0x622e4d str pos: 0x622fb2 length: 17
pub: %v
root: %v


key pos: 0x619693 str pos: 0x6198c1 length: 9
\Desktop\

key pos: 0x617561 str pos: 0x61755d length: 1
\

key pos: 0x618665 str pos: 0x6185d2 length: 7
Global\

key pos: 0x617e27 str pos: 0x617ea9 length: 5
netsh

key pos: 0x61bb88 str pos: 0x61c415 length: 11
advfirewall

key pos: 0x617817 str pos: 0x6177cc length: 3
set

key pos: 0x61b327 str pos: 0x61b655 length: 11
allprofiles

key pos: 0x6206a5 str pos: 0x620dcf length: 14
firewallpolicy

key pos: 0x629001 str pos: 0x628e13 length: 26
blockinbound,blockoutbound

key pos: 0x617ce2 str pos: 0x617d78 length: 5
netsh

key pos: 0x61bbd5 str pos: 0x61c441 length: 11
advfirewall

key pos: 0x6176d6 str pos: 0x61770c length: 3
set

key pos: 0x61b353 str pos: 0x61b0eb length: 11
allprofiles

key pos: 0x617ec7 str pos: 0x617de6 length: 5
state

key pos: 0x61757f str pos: 0x6175ad length: 2
on

key pos: 0x617d9b str pos: 0x617ef9 length: 5
netsh

key pos: 0x61b5dc str pos: 0x61b24b length: 11
advfirewall

key pos: 0x6177f3 str pos: 0x61785f length: 3
set

key pos: 0x61c134 str pos: 0x61be27 length: 11
allprofiles

key pos: 0x617e18 str pos: 0x617e9f length: 5
state

key pos: 0x617814 str pos: 0x6177c9 length: 3
off

key pos: 0x62e5de str pos: 0x62e609 length: 43
select DomainRole FROM Win32_ComputerSystem

key pos: 0x6238ee str pos: 0x623f42 length: 18
CoUninitialize %v


key pos: 0x62b8e7 str pos: 0x62b847 length: 32
WbemScripting.SWbemNamedValueSet

key pos: 0x6228f0 str pos: 0x621ec0 length: 16
CreateObject %v


key pos: 0x623774 str pos: 0x623c06 length: 18
QueryInterface %v


key pos: 0x6177db str pos: 0x6177ff length: 3
Add

key pos: 0x6269ac str pos: 0x626b64 length: 22
__ProviderArchitecture

key pos: 0x629271 str pos: 0x629105 length: 26
CallMethod architecture%v


key pos: 0x62901b str pos: 0x62904f length: 26
WbemScripting.SWbemLocator

key pos: 0x621dd0 str pos: 0x6227e0 length: 16
CreateObject %v


key pos: 0x6237e0 str pos: 0x62358e length: 18
QueryInterface %v


key pos: 0x61f978 str pos: 0x61f6e1 length: 13
ConnectServer

key pos: 0x61a8aa str pos: 0x61a9d6 length: 10
root\cimv2

key pos: 0x62a185 str pos: 0x629d79 length: 28
CallMethod ConnectServer %v


key pos: 0x619195 str pos: 0x619a9e length: 9
ExecQuery

key pos: 0x62ae97 str pos: 0x62ada7 length: 30
SELECT * FROM Win32_ShadowCopy

key pos: 0x620501 str pos: 0x620811 length: 14
CallMethod %v


key pos: 0x617ed1 str pos: 0x617e63 length: 5
Count

key pos: 0x6261dc str pos: 0x625a65 length: 21
GetProperty Count %v


key pos: 0x61938d str pos: 0x61953d length: 9
ItemIndex

key pos: 0x62003f str pos: 0x620d89 length: 14
CallMethod %v


key pos: 0x6175b1 str pos: 0x617621 length: 2
ID

key pos: 0x62369c str pos: 0x6237f2 length: 18
GetProperty ID %v


key pos: 0x618944 str pos: 0x6186c0 length: 7
Delete_

key pos: 0x617e9a str pos: 0x617e59 length: 5
\temp

key pos: 0x617db9 str pos: 0x617ca6 length: 5
.docx

key pos: 0x618044 str pos: 0x618278 length: 6
.accdb

key pos: 0x6181f4 str pos: 0x6181ca length: 6
.accde

key pos: 0x6182fc str pos: 0x61820c length: 6
.accdr

key pos: 0x6181ee str pos: 0x6181d0 length: 6
.accdt

key pos: 0x617ac8 str pos: 0x617b88 length: 4
.asp

key pos: 0x617e09 str pos: 0x617e4f length: 5
.aspx

key pos: 0x617dd7 str pos: 0x617e45 length: 5
.back

key pos: 0x6187a7 str pos: 0x61877d length: 7
.backup

key pos: 0x619c21 str pos: 0x6193f9 length: 9
.backupdb

key pos: 0x6178c8 str pos: 0x6179d0 length: 4
.bak

key pos: 0x6178b4 str pos: 0x6179d4 length: 4
.mdb

key pos: 0x617b54 str pos: 0x617934 length: 4
.mdc

key pos: 0x617a2c str pos: 0x617a04 length: 4
.mdf

key pos: 0x6178d0 str pos: 0x6179c8 length: 4
.war

key pos: 0x617a20 str pos: 0x617a40 length: 4
.xls

key pos: 0x617e5e str pos: 0x617e04 length: 5
.xlsx

key pos: 0x617e4a str pos: 0x617e1d length: 5
.xlsm

key pos: 0x617acc str pos: 0x617980 length: 4
.xlr

key pos: 0x617994 str pos: 0x617be4 length: 4
.zip

key pos: 0x617a58 str pos: 0x617bf8 length: 4
.rar

key pos: 0x61991b str pos: 0x6199ea length: 9
.sqlitedb

key pos: 0x617a48 str pos: 0x617a10 length: 4
.sql

key pos: 0x61780b str pos: 0x617862 length: 3
.py

key pos: 0x617d82 str pos: 0x617f8a length: 5
.ppam

key pos: 0x617aa8 str pos: 0x617a7c length: 4
.pps

key pos: 0x617da0 str pos: 0x617c6a length: 5
.ppsm

key pos: 0x617c65 str pos: 0x617daa length: 5
.ppsx

key pos: 0x617bd0 str pos: 0x6179b0 length: 4
.ppt

key pos: 0x6179f0 str pos: 0x617b60 length: 4
pptm

key pos: 0x617e31 str pos: 0x617df5 length: 5
.pptx

key pos: 0x617ab4 str pos: 0x617a78 length: 4
.hpp

key pos: 0x617e68 str pos: 0x617dff length: 5
.java

key pos: 0x617a98 str pos: 0x617a5c length: 4
.jsp

key pos: 0x617a6c str pos: 0x617a84 length: 4
.php

key pos: 0x6178ec str pos: 0x6179c4 length: 4
.doc

key pos: 0x617d91 str pos: 0x617da5 length: 5
.docm

key pos: 0x617ab8 str pos: 0x617a70 length: 4
.pst

key pos: 0x617b70 str pos: 0x617ac4 length: 4
.psd

key pos: 0x617958 str pos: 0x617b14 length: 4
.dot

key pos: 0x617ad4 str pos: 0x6179d8 length: 4
dotm

key pos: 0x6179e8 str pos: 0x6178f8 length: 4
.cpp

key pos: 0x617808 str pos: 0x617802 length: 3
.cs

key pos: 0x6179dc str pos: 0x617908 length: 4
.csv

key pos: 0x617bf0 str pos: 0x617a8c length: 4
.bkp

key pos: 0x6177d2 str pos: 0x6176e2 length: 3
.db

key pos: 0x61be95 str pos: 0x61bb9e length: 11
.db-journal

key pos: 0x61871b str pos: 0x618688 length: 7
.csproj

key pos: 0x617a0c str pos: 0x617a50 length: 4
.sln

key pos: 0x617751 str pos: 0x617820 length: 3
.md

key pos: 0x6177de str pos: 0x6177f9 length: 3
.pl

key pos: 0x6177cf str pos: 0x6176df length: 3
.js

key pos: 0x617dd2 str pos: 0x617cc9 length: 5
.html

key pos: 0x6179f4 str pos: 0x6178f4 length: 4
.htm

key pos: 0x6178a0 str pos: 0x6179bc length: 4
.dbf

key pos: 0x617bec str pos: 0x617aa0 length: 4
.rdo

key pos: 0x617bf4 str pos: 0x617a88 length: 4
.arc

key pos: 0x617a24 str pos: 0x6179fc length: 4
.vhd

key pos: 0x617daf str pos: 0x617cba length: 5
.vmdk

key pos: 0x617be8 str pos: 0x617a9c length: 4
.vdi

key pos: 0x617e90 str pos: 0x617ecc length: 5
.vhdx

key pos: 0x617a18 str pos: 0x617a3c length: 4
.edb

key pos: 0x617653 str pos: 0x61762f length: 2
.c

key pos: 0x61762b str pos: 0x61762d length: 2
.h

key pos: 0x617b74 str pos: 0x617ac0 length: 4
.dll

key pos: 0x617a14 str pos: 0x617a4c length: 4
.exe

key pos: 0x617bc0 str pos: 0x6179ac length: 4
.sys

key pos: 0x61798c str pos: 0x617bdc length: 4
.mui

key pos: 0x6178fc str pos: 0x6179ec length: 4
.tmp

key pos: 0x617a1c str pos: 0x617a44 length: 4
.lnk

key pos: 0x61863b str pos: 0x61845f length: 7
.config

key pos: 0x619912 str pos: 0x6199f3 length: 9
.manifest

key pos: 0x617be0 str pos: 0x617990 length: 4
.tlb

key pos: 0x617a94 str pos: 0x617a64 length: 4
.olb

key pos: 0x617a00 str pos: 0x617a28 length: 4
.blf

key pos: 0x617a08 str pos: 0x617a54 length: 4
.ico

key pos: 0x61d357 str pos: 0x61d28b length: 12
.regtrans-ms

key pos: 0x623f1e str pos: 0x623666 length: 18
.devicemetadata-ms

key pos: 0x623a56 str pos: 0x623924 length: 18
.settingcontent-ms

key pos: 0x617a60 str pos: 0x617a90 length: 4
.bat

key pos: 0x6179e4 str pos: 0x617900 length: 4
.cmd

key pos: 0x617ab0 str pos: 0x617a74 length: 4
.ps1

key pos: 0x61ba33 str pos: 0x61c2d6 length: 11
desktop.ini

key pos: 0x61dd83 str pos: 0x61e107 length: 12
iconcache.db

key pos: 0x61a422 str pos: 0x61ae9a length: 10
ntuser.dat

key pos: 0x61a8d2 str pos: 0x61a7b0 length: 10
ntuser.ini

key pos: 0x6219ea str pos: 0x6214fe length: 15
ntuser.dat.log1

key pos: 0x62150d str pos: 0x6219db length: 15
ntuser.dat.log2

key pos: 0x61ee27 str pos: 0x61e06b length: 12
usrclass.dat

key pos: 0x622b61 str pos: 0x622a1e length: 17
usrclass.dat.log1

key pos: 0x622e1a str pos: 0x622fc3 length: 17
usrclass.dat.log2

key pos: 0x61838d str pos: 0x6184eb length: 7
bootmgr

key pos: 0x618642 str pos: 0x61890c length: 7
bootnxt

key pos: 0x61822a str pos: 0x6181ac length: 6
windir

key pos: 0x61b2e5 str pos: 0x61c6ca length: 11
SystemDrive

key pos: 0x6207d9 str pos: 0x620a41 length: 14
:\$Recycle.Bin

key pos: 0x61fa55 str pos: 0x61f84d length: 13
:\ProgramData

key pos: 0x6231e3 str pos: 0x622cb5 length: 17
:\Users\All Users

key pos: 0x621c9c str pos: 0x620fb8 length: 15
:\Program Files

key pos: 0x622630 str pos: 0x622490 length: 16
:\Local Settings

key pos: 0x6182e4 str pos: 0x6180bc length: 6
:\Boot

key pos: 0x62989d str pos: 0x629909 length: 27
:\System Volume Information

key pos: 0x61ac7e str pos: 0x61ad0a length: 10
:\Recovery

key pos: 0x6191dd str pos: 0x619b9a length: 9
\AppData\

key pos: 0x617ebd str pos: 0x617e0e length: 5
ntldr

key pos: 0x61d54f str pos: 0x61cdcf length: 12
NTDETECT.COM

key pos: 0x618c70 str pos: 0x618a58 length: 8
boot.ini

key pos: 0x61cb2f str pos: 0x61cf1f length: 12
bootfont.bin

key pos: 0x61e0d7 str pos: 0x61dc63 length: 12
bootsect.bak

key pos: 0x61c877 str pos: 0x61b8d3 length: 11
desktop.ini

key pos: 0x61a33c str pos: 0x61ad5a length: 10
ctfmon.exe

key pos: 0x61e017 str pos: 0x61e317 length: 12
iconcache.db

key pos: 0x61a8f0 str pos: 0x61a77e length: 10
ntuser.dat

key pos: 0x6208ab str pos: 0x620777 length: 14
ntuser.dat.log

key pos: 0x61a5b2 str pos: 0x61aa8a length: 10
ntuser.ini

key pos: 0x619534 str pos: 0x619b6d length: 9
thumbs.db

key pos: 0x630990 str pos: 0x630930 length: 96
.+\\Microsoft\\(User Account Pictures|Windows\\(Explorer|Caches)|Device Stage\\Device|Windows)\\

key pos: 0x622963 str pos: 0x622b0c length: 17
already encrypted

key pos: 0x628aa0 str pos: 0x62869f length: 25
worker %s started job %s


key pos: 0x62887a str pos: 0x6286d1 length: 25
error encrypting %v : %v


key pos: 0x617568 str pos: 0x617557 length: 1
\

key pos: 0x617565 str pos: 0x61755b length: 1
\

key pos: 0x626b38 str pos: 0x626a04 length: 22
There can be only one


key pos: 0x630e78 str pos: 0x631022 length: 426
-----BEGIN RSA PUBLIC KEY-----
MIIBCgKCAQEAnqjO7EYoSfxESLO7yAoCLOXxdR9N8wVkgRuKM84ie1MAEkB0Nlsy
eLhEMoAeUEDyVAML4gtwjKDX3eVs7nrmk3wRcq8nU803fq9fYu57EYAXZpb40srq
FpiVnDZ1vB47MMhn7oHepbQ/pHhItU7evgmyB5s8J80hnDg5eQfnAdPmLPO/S3fs
DT5KL0Y0x2S14q0jBKgUiL0ZhdqqHUTchFPSVid0U8AKOidJwhpz+j9J2jUZ2M2t
njdXbOU06R8NFAoJSxY7T9nY7FA0SNqL9N/V9sThDIoLpCn8RanUb0jZzoEFqWrf
Hsr1l/5F235OMmIr+YuWnMl5kSNlLO551QIDAQAB
-----END RSA PUBLIC KEY-----


key pos: 0x618bf8 str pos: 0x618a30 length: 8
bad pem


key pos: 0x6177ea str pos: 0x6177fc length: 3
%v


key pos: 0x6177e4 str pos: 0x6177f0 length: 3
%v


key pos: 0x61bfc9 str pos: 0x61bc2d length: 11
ccflic0.exe

key pos: 0x61bdda str pos: 0x61c129 length: 11
ccflic4.exe

key pos: 0x622ac8 str pos: 0x622ce8 length: 17
healthservice.exe

key pos: 0x620e8c str pos: 0x620fa9 length: 15
ilicensesvc.exe

key pos: 0x61acce str pos: 0x61a2d8 length: 10
nimbus.exe

key pos: 0x6223e0 str pos: 0x622920 length: 16
prlicensemgr.exe

key pos: 0x627100 str pos: 0x6273e0 length: 23
certificateprovider.exe

key pos: 0x629975 str pos: 0x6298ee length: 27
proficypublisherservice.exe

key pos: 0x620aa3 str pos: 0x6203f7 length: 14
proficysts.exe

key pos: 0x61a1e8 str pos: 0x619edc length: 10
erlsrv.exe

key pos: 0x61cfbb str pos: 0x61cd87 length: 12
vmtoolsd.exe

key pos: 0x627636 str pos: 0x62750b length: 23
managementagenthost.exe

key pos: 0x622e91 str pos: 0x623029 length: 17
vgauthservice.exe

key pos: 0x618e90 str pos: 0x618df0 length: 8
epmd.exe

key pos: 0x61bb30 str pos: 0x61c483 length: 11
hasplmv.exe

key pos: 0x61c974 str pos: 0x61bb93 length: 11
spooler.exe

key pos: 0x61869d str pos: 0x618799 length: 7
hdb.exe

key pos: 0x620785 str pos: 0x620881 length: 14
ntservices.exe

key pos: 0x617f94 str pos: 0x617dc3 length: 5
n.exe

key pos: 0x623d92 str pos: 0x6237aa length: 18
monitoringhost.exe

key pos: 0x621f50 str pos: 0x621e30 length: 16
win32sysinfo.exe

key pos: 0x622320 str pos: 0x622620 length: 16
inet_gethost.exe

key pos: 0x61f339 str pos: 0x61fcc5 length: 13
taskhostw.exe

key pos: 0x6283fc str pos: 0x628492 length: 25
proficy administrator.exe

key pos: 0x6197fb str pos: 0x619909 length: 9
ntevl.exe

key pos: 0x622480 str pos: 0x622900 length: 16
prproficymgr.exe

key pos: 0x6191e6 str pos: 0x619a4d length: 9
prrds.exe

key pos: 0x61d453 str pos: 0x61ec0b length: 12
prrouter.exe

key pos: 0x62131e str pos: 0x621a62 length: 15
prconfigmgr.exe

key pos: 0x61fafe str pos: 0x61f43d length: 13
prgateway.exe

key pos: 0x623018 str pos: 0x622ec4 length: 17
premailengine.exe

key pos: 0x61fe71 str pos: 0x620299 length: 14
pralarmmgr.exe

key pos: 0x621549 str pos: 0x621945 length: 15
prftpengine.exe

key pos: 0x625894 str pos: 0x625240 length: 20
prcalculationmgr.exe

key pos: 0x622eb3 str pos: 0x622ff6 length: 17
prprintserver.exe

key pos: 0x622c0b str pos: 0x622a73 length: 17
prdatabasemgr.exe

key pos: 0x6203db str pos: 0x620379 length: 14
preventmgr.exe

key pos: 0x61d2f7 str pos: 0x61ed2b length: 12
prreader.exe

key pos: 0x61ed67 str pos: 0x61d3c3 length: 12
prwriter.exe

key pos: 0x622410 str pos: 0x622530 length: 16
prsummarymgr.exe

key pos: 0x61f645 str pos: 0x61f985 length: 13
prstubber.exe

key pos: 0x622aa6 str pos: 0x622c4f length: 17
prschedulemgr.exe

key pos: 0x61836a str pos: 0x6184a5 length: 7
cdm.exe

key pos: 0x626341 str pos: 0x625e01 length: 21
musnotificationux.exe

key pos: 0x61f4b2 str pos: 0x61f99f length: 13
npmdagent.exe

key pos: 0x61d963 str pos: 0x61e5ab length: 12
client64.exe

key pos: 0x61ab2a str pos: 0x61a4fe length: 10
keysvc.exe

key pos: 0x624470 str pos: 0x624a73 length: 19
server_eventlog.exe

key pos: 0x623337 str pos: 0x622d4e length: 17
proficyserver.exe

key pos: 0x623be2 str pos: 0x623900 length: 18
server_runtime.exe

key pos: 0x626a5c str pos: 0x626b4e length: 22
config_api_service.exe

key pos: 0x627539 str pos: 0x627664 length: 23
fnplicensingservice.exe

key pos: 0x625268 str pos: 0x6255c4 length: 20
workflowresttest.exe

key pos: 0x622fd4 str pos: 0x622e5e length: 17
proficyclient.exe

key pos: 0x61ee1b str pos: 0x61de8b length: 12
vmacthlp.exe

key pos: 0x61fdbc str pos: 0x61f568 length: 13
msdtssrvr.exe

key pos: 0x61e197 str pos: 0x61df93 length: 12
sqlservr.exe

key pos: 0x61bef8 str pos: 0x61c14a length: 11
msmdsrv.exe

key pos: 0x62a051 str pos: 0x62a115 length: 28
reportingservicesservice.exe

key pos: 0x61bcc7 str pos: 0x61c08f length: 11
dsmcsvc.exe

key pos: 0x61be32 str pos: 0x61c8da length: 11
winvnc4.exe

key pos: 0x61a706 str pos: 0x61a90e length: 10
client.exe

key pos: 0x61ea7f str pos: 0x61d423 length: 12
collwrap.exe

key pos: 0x627498 str pos: 0x627a86 length: 23
bluestripecollector.exe

key pos: 0x620077 str pos: 0x61ff7b length: 14
sqlbrowser.exe

key pos: 0x61ab98 str pos: 0x61a65c length: 10
dsmcad.exe

key pos: 0x6209d1 str pos: 0x6204ad length: 14
nimcluster.exe

key pos: 0x6225f0 str pos: 0x622300 length: 16
googleupdate.exe

key pos: 0x6187ae str pos: 0x6186d5 length: 7
smc.exe

key pos: 0x620459 str pos: 0x620cb7 length: 14
bcrservice.exe

key pos: 0x61aa1c str pos: 0x61a81e length: 10
dbsrv9.exe

key pos: 0x61c2aa str pos: 0x61bb72 length: 11
rtvscan.exe

key pos: 0x620a17 str pos: 0x6205d3 length: 14
bcreporter.exe

key pos: 0x61c42b str pos: 0x61bbeb length: 11
csadmin.exe

key pos: 0x61dd5f str pos: 0x61e143 length: 12
csdbsync.exe

key pos: 0x619b0a str pos: 0x6194ec length: 9
csmon.exe

key pos: 0x619db0 str pos: 0x61a026 length: 10
csauth.exe

key pos: 0x619c96 str pos: 0x6197a1 length: 9
cslog.exe

key pos: 0x61d5c7 str pos: 0x61ec83 length: 12
csradius.exe

key pos: 0x61e6e3 str pos: 0x61db43 length: 12
cstacacs.exe

key pos: 0x6221f0 str pos: 0x6228c0 length: 16
url_response.exe

key pos: 0x62696a str pos: 0x626bfe length: 22
vmware-converter-a.exe

key pos: 0x624e30 str pos: 0x625178 length: 20
vmware-converter.exe

key pos: 0x61c0a5 str pos: 0x61bd1f length: 11
avagent.exe

key pos: 0x62a7d8 str pos: 0x62a79e length: 29
paxton.net2.clientservice.exe

key pos: 0x62c2ef str pos: 0x62c3dd length: 34
paxton.net2.commsserverservice.exe

key pos: 0x619c69 str pos: 0x6195f1 length: 9
avscc.exe

key pos: 0x61b870 str pos: 0x61c4f1 length: 11
prunsrv.exe

key pos: 0x626bbc str pos: 0x626954 length: 22
googlecrashhandler.exe

key pos: 0x627bce str pos: 0x628066 length: 24
googlecrashhandler64.exe

key pos: 0x61fe9b str pos: 0x620237 length: 14
vmwaretray.exe

key pos: 0x61add2 str pos: 0x61a472 length: 10
nd2svc.exe

key pos: 0x61c672 str pos: 0x61b941 length: 11
tnslsnr.exe

key pos: 0x61dcab str pos: 0x61e233 length: 12
omtsreco.exe

key pos: 0x61abe8 str pos: 0x61a634 length: 10
oracle.exe

key pos: 0x620f5e str pos: 0x62112f length: 15
patrolagent.exe

key pos: 0x621d14 str pos: 0x621585 length: 15
scfagent_64.exe

key pos: 0x62090d str pos: 0x620571 length: 14
patrolperf.exe

key pos: 0x61c0dc str pos: 0x61bc43 length: 11
rscdsvc.exe

key pos: 0x618c68 str pos: 0x6189e8 length: 8
rscd.exe

key pos: 0x61f242 str pos: 0x61eef5 length: 13
pmgreader.exe

key pos: 0x61b978 str pos: 0x61c247 length: 11
firefox.exe

key pos: 0x61a364 str pos: 0x61acd8 length: 10
chrome.exe

key pos: 0x623ad4 str pos: 0x6239b4 length: 18
netsession_win.exe

key pos: 0x61966f str pos: 0x619a29 length: 9
pcsws.exe

key pos: 0x6191b0 str pos: 0x61942f length: 9
pcscm.exe

key pos: 0x61d7cb str pos: 0x61e45b length: 12
cwbunnav.exe

key pos: 0x61aef4 str pos: 0x61a328 length: 10
rdrcef.exe

key pos: 0x61996c str pos: 0x61965d length: 9
ndrvx.exe

key pos: 0x619cc3 str pos: 0x619681 length: 9
ndrvs.exe

key pos: 0x625538 str pos: 0x625420 length: 20
dr_serviceengine.exe

key pos: 0x626a72 str pos: 0x626aca length: 22
teamviewer_service.exe

key pos: 0x61d897 str pos: 0x61e737 length: 12
sqlagent.exe

key pos: 0x61a774 str pos: 0x61a954 length: 10
dwrcst.exe

key pos: 0x6233ae str pos: 0x622dc5 length: 17
ccm messaging.exe

key pos: 0x619c84 str pos: 0x619828 length: 9
zoolz.exe

key pos: 0x61c365 str pos: 0x61bb0f length: 11
agntsvc.exe

key pos: 0x61c738 str pos: 0x61b8b2 length: 11
dbeng50.exe

key pos: 0x619ef0 str pos: 0x61a170 length: 10
dbsnmp.exe

key pos: 0x61aa26 str pos: 0x61a800 length: 10
encsvc.exe

key pos: 0x619a44 str pos: 0x61927f length: 9
excel.exe

key pos: 0x622f3b str pos: 0x622f6e length: 17
firefoxconfig.exe

key pos: 0x61e15b str pos: 0x61dc33 length: 12
infopath.exe

key pos: 0x6215ee str pos: 0x6217b0 length: 15
isqlplussvc.exe

key pos: 0x61e497 str pos: 0x61d94b length: 12
msaccess.exe

key pos: 0x61eca7 str pos: 0x61d66f length: 12
msftesql.exe

key pos: 0x619be2 str pos: 0x6195c4 length: 9
mspub.exe

key pos: 0x622380 str pos: 0x6225c0 length: 16
mydesktopqos.exe

key pos: 0x625560 str pos: 0x6252e0 length: 20
mydesktopservice.exe

key pos: 0x61ab7a str pos: 0x61a6a2 length: 10
mysqld.exe

key pos: 0x61f527 str pos: 0x61f96b length: 13
mysqld-nt.exe

key pos: 0x61feef str pos: 0x62011f length: 14
mysqld-opt.exe

key pos: 0x6203a3 str pos: 0x620c2b length: 14
ocautoupds.exe

key pos: 0x619522 str pos: 0x619b2e length: 9
ocomm.exe

key pos: 0x6196ae str pos: 0x619a17 length: 9
ocssd.exe

key pos: 0x61b516 str pos: 0x61b2b9 length: 11
onenote.exe

key pos: 0x61b920 str pos: 0x61c790 length: 11
outlook.exe

key pos: 0x61e6ef str pos: 0x61d873 length: 12
powerpnt.exe

key pos: 0x623b52 str pos: 0x6239ea length: 18
sqbcoreservice.exe

key pos: 0x61f054 str pos: 0x61f117 length: 13
sqlwriter.exe

key pos: 0x619ae6 str pos: 0x619585 length: 9
steam.exe

key pos: 0x61d09f str pos: 0x61d2af length: 12
synctime.exe

key pos: 0x621b7f str pos: 0x621387 length: 15
tbirdconfig.exe

key pos: 0x61aa30 str pos: 0x61a76a length: 10
thebat.exe

key pos: 0x61e287 str pos: 0x61dccf length: 12
thebat64.exe

key pos: 0x621594 str pos: 0x62180a length: 15
thunderbird.exe

key pos: 0x619546 str pos: 0x619c0f length: 9
visio.exe

key pos: 0x61b7f7 str pos: 0x61c743 length: 11
winword.exe

key pos: 0x61c84b str pos: 0x61b710 length: 11
wordpad.exe

key pos: 0x61f0d6 str pos: 0x61f13e length: 13
xfssvccon.exe

key pos: 0x61e75b str pos: 0x61d7fb length: 12
tmlisten.exe

key pos: 0x61e6cb str pos: 0x61d85b length: 12
pccntmon.exe

key pos: 0x61f47e str pos: 0x61fcd2 length: 13
cntaosmgr.exe

key pos: 0x61cd9f str pos: 0x61d093 length: 12
ntrtscan.exe

key pos: 0x61cd03 str pos: 0x61d183 length: 12
mbamtray.exe

key pos: 0x62451b str pos: 0x6248f7 length: 19
qhactivedefense.exe

key pos: 0x62020d str pos: 0x61fe63 length: 14
qhwatchdog.exe

key pos: 0x62057f str pos: 0x620929 length: 14
qhsafetray.exe

key pos: 0x61a8a0 str pos: 0x61aa62 length: 10
avgsvc.exe

key pos: 0x6193ba str pos: 0x61922e length: 9
avgui.exe

key pos: 0x61af94 str pos: 0x61a878 length: 10
v3lite.exe

key pos: 0x61abb6 str pos: 0x61a4b8 length: 10
v3main.exe

key pos: 0x618a68 str pos: 0x618bc8 length: 8
v3sp.exe

key pos: 0x61b6ad str pos: 0x61c6eb length: 11
avastui.exe

key pos: 0x61cb0b str pos: 0x61cf37 length: 12
avastsvc.exe

key pos: 0x61b3ed str pos: 0x61b101 length: 11
avguard.exe

key pos: 0x61ce3b str pos: 0x61caab length: 12
avshadow.exe

key pos: 0x619a0e str pos: 0x6196c0 length: 9
avgnt.exe

key pos: 0x625ba0 str pos: 0x625a3b length: 21
avira.servicehost.exe

key pos: 0x622996 str pos: 0x622b2e length: 17
avira.systray.exe

key pos: 0x61b660 str pos: 0x61b2cf length: 11
bdagent.exe

key pos: 0x61f826 str pos: 0x61f6ee length: 13
bdredline.exe

key pos: 0x619078 str pos: 0x618d08 length: 8
bdss.exe

key pos: 0x627481 str pos: 0x62774a length: 23
bullguardbhvscanner.exe

key pos: 0x6251f0 str pos: 0x6258a8 length: 20
bullguardscanner.exe

key pos: 0x622ee6 str pos: 0x6233e1 length: 17
bullguardtray.exe

key pos: 0x624cf9 str pos: 0x62445d length: 19
bullguardupdate.exe

key pos: 0x61f088 str pos: 0x61f2de length: 13
bullguard.exe

key pos: 0x61d7bf str pos: 0x61e443 length: 12
cmdagent.exe

key pos: 0x61c60f str pos: 0x61b7d6 length: 11
cistray.exe

key pos: 0x618729 str pos: 0x618784 length: 7
cis.exe

key pos: 0x621cba str pos: 0x621279 length: 15
spideragent.exe

key pos: 0x61d807 str pos: 0x61e53f length: 12
dwengine.exe

key pos: 0x620e7d str pos: 0x6210d5 length: 15
dwarkdaemon.exe

key pos: 0x621300 str pos: 0x621b16 length: 15
dwnetfilter.exe

key pos: 0x61f534 str pos: 0x61f95e length: 13
a2service.exe

key pos: 0x62788c str pos: 0x62743c length: 23
a2guard.exe.a2start.exe

key pos: 0x6189f0 str pos: 0x618ac8 length: 8
egui.exe

key pos: 0x618e50 str pos: 0x618ed0 length: 8
ekrn.exe

key pos: 0x61fea9 str pos: 0x6200bd length: 14
fshoster32.exe

key pos: 0x620651 str pos: 0x6207af length: 14
fshoster64.exe

key pos: 0x62608c str pos: 0x625fa5 length: 21
fortisslvpndaemon.exe

key pos: 0x62050f str pos: 0x6209c3 length: 14
fortiesnac.exe

key pos: 0x61c95e str pos: 0x61bf45 length: 11
fortiwf.exe

key pos: 0x61efdf str pos: 0x61f1cd length: 13
fortitray.exe

key pos: 0x620723 str pos: 0x620873 length: 14
fchelper64.exe

key pos: 0x6206cf str pos: 0x6208b9 length: 14
fortiproxy.exe

key pos: 0x61b773 str pos: 0x61b8e9 length: 11
fcappdb.exe

key pos: 0x61c667 str pos: 0x61b844 length: 11
fcdblog.exe

key pos: 0x61854d str pos: 0x6183da length: 7
avp.exe

key pos: 0x61976b str pos: 0x619879 length: 9
avpui.exe

key pos: 0x620f22 str pos: 0x6211e3 length: 15
mbamservice.exe

key pos: 0x61d0cf str pos: 0x61cdab length: 12
mcsacore.exe

key pos: 0x61b999 str pos: 0x61c2cb length: 11
mcapexe.exe

key pos: 0x61e3fb str pos: 0x61d9e7 length: 12
mcshield.exe

key pos: 0x61d543 str pos: 0x61e9d7 length: 12
mcsvhost.exe

key pos: 0x62360c str pos: 0x62344a length: 18
nortonsecurity.exe

key pos: 0x621297 str pos: 0x621cd8 length: 15
psuaservice.exe

key pos: 0x61e137 str pos: 0x61def7 length: 12
psuamain.exe

key pos: 0x61d813 str pos: 0x61e6b3 length: 12
psanhost.exe

key pos: 0x6201d5 str pos: 0x620023 length: 14
sdrservice.exe

key pos: 0x621378 str pos: 0x621abc length: 15
swc_service.exe

key pos: 0x6215a3 str pos: 0x621d05 length: 15
swi_service.exe

key pos: 0x618730 str pos: 0x618768 length: 7
ssp.exe

key pos: 0x61caff str pos: 0x61cf8b length: 12
ccsvchst.exe

key pos: 0x61a594 str pos: 0x61ac2e length: 10
smcgui.exe

key pos: 0x625830 str pos: 0x62518c length: 20
coreserviceshell.exe

key pos: 0x625bf4 str pos: 0x625ace length: 21
coreframeworkhost.exe

key pos: 0x6206eb str pos: 0x620db3 length: 14
uiwatchdog.exe

key pos: 0x61d033 str pos: 0x61ccf7 length: 12
uiseagnt.exe

key pos: 0x61ba80 str pos: 0x61c462 length: 11
paamsrv.exe

key pos: 0x61c856 str pos: 0x61b6d9 length: 11
psh_svc.exe

key pos: 0x61be11 str pos: 0x61c108 length: 11
aupdrun.exe

key pos: 0x6198d3 str pos: 0x6197e9 length: 9
acaas.exe

key pos: 0x61d3db str pos: 0x61d753 length: 12
acaegmgr.exe

key pos: 0x619951 str pos: 0x61960c length: 9
acaif.exe

key pos: 0x619426 str pos: 0x619276 length: 9
acais.exe

key pos: 0x619975 str pos: 0x619615 length: 9
ahnsd.exe

key pos: 0x61c8ae str pos: 0x61bc4e length: 11
ahnsdsv.exe

key pos: 0x61ad14 str pos: 0x61a396 length: 10
autoup.exe

key pos: 0x61e23f str pos: 0x61dfab length: 12
v3clnsrv.exe

key pos: 0x61c160 str pos: 0x61bc22 length: 11
v3medic.exe

key pos: 0x6196a5 str pos: 0x619948 length: 9
v3svc.exe

key pos: 0x61b117 str pos: 0x61b3f8 length: 11
aflogvw.exe

key pos: 0x61a47c str pos: 0x61af44 length: 10
ahnrpt.exe

key pos: 0x61edd3 str pos: 0x61d717 length: 12
atwsctsk.exe

key pos: 0x61abd4 str pos: 0x61a58a length: 10
v3exec.exe

key pos: 0x61ba8b str pos: 0x61c3e9 length: 11
v3imscn.exe

key pos: 0x61de43 str pos: 0x61d3f3 length: 12
monsvcnt.exe

key pos: 0x61d8df str pos: 0x61e5c3 length: 12
monsysnt.exe

key pos: 0x620eaa str pos: 0x621120 length: 15
aexnsrcvsvc.exe

key pos: 0x619d1a str pos: 0x619f90 length: 10
aexsvc.exe

key pos: 0x61d6ab str pos: 0x61ed97 length: 12
atrshost.exe

key pos: 0x620d51 str pos: 0x620475 length: 14
ctdataload.exe

key pos: 0x623990 str pos: 0x623a8c length: 18
aexagentuihost.exe

key pos: 0x62089d str pos: 0x620769 length: 14
aexnsagent.exe

key pos: 0x61df7b str pos: 0x61e32f length: 12
aclntusr.exe

key pos: 0x61f44a str pos: 0x61fcb8 length: 13
aexswdusr.exe

key pos: 0x61d237 str pos: 0x61cb5f length: 12
pxemtftp.exe

key pos: 0x61bf0e str pos: 0x61c18c length: 11
aclient.exe

key pos: 0x6239a2 str pos: 0x623b1c length: 18
securitycenter.exe

key pos: 0x61aeb8 str pos: 0x61a346 length: 10
starta.exe

key pos: 0x6191ef str pos: 0x619a56 length: 9
stopa.exe

key pos: 0x61973e str pos: 0x619855 length: 9
anvir.exe

key pos: 0x61e797 str pos: 0x61db97 length: 12
csrss_tc.exe

key pos: 0x61e4c7 str pos: 0x61d843 length: 12
ashavast.exe

key pos: 0x61a666 str pos: 0x61abfc length: 10
ashbug.exe

key pos: 0x61d76b str pos: 0x61d3cf length: 12
ashchest.exe

key pos: 0x61ad78 str pos: 0x61a2f6 length: 10
ashcmd.exe

key pos: 0x61bee2 str pos: 0x61c1a2 length: 11
ashdisp.exe

key pos: 0x61ee33 str pos: 0x61dda7 length: 12
ashenhcd.exe

key pos: 0x61c11e str pos: 0x61be3d length: 11
ashlogv.exe

key pos: 0x61e323 str pos: 0x61dedf length: 12
ashmaisv.exe

key pos: 0x61dc7b str pos: 0x61e09b length: 12
ashpopwz.exe

key pos: 0x61dc57 str pos: 0x61e08f length: 12
ashquick.exe

key pos: 0x61bd61 str pos: 0x61c0bb length: 11
ashserv.exe

key pos: 0x61d513 str pos: 0x61ea5b length: 12
ashsimp2.exe

key pos: 0x61e047 str pos: 0x61e39b length: 12
ashsimpl.exe

key pos: 0x61dbaf str pos: 0x61e7eb length: 12
ashskpcc.exe

key pos: 0x61da0b str pos: 0x61e623 length: 12
ashskpck.exe

key pos: 0x61a3c8 str pos: 0x61ae18 length: 10
ashupd.exe

key pos: 0x61ea97 str pos: 0x61d3b7 length: 12
ashwebsv.exe

key pos: 0x61c00b str pos: 0x61bc7a length: 11
aswdisp.exe

key pos: 0x61f749 str pos: 0x61f867 length: 13
aswregsvr.exe

key pos: 0x61b14e str pos: 0x61b4df length: 11
aswserv.exe

key pos: 0x61de67 str pos: 0x61e293 length: 12
aswupdsv.exe

key pos: 0x61e767 str pos: 0x61db73 length: 12
aswwebsv.exe

key pos: 0x61e383 str pos: 0x61dfcf length: 12
avengine.exe

key pos: 0x61b4a8 str pos: 0x61b17a length: 11
afwserv.exe

key pos: 0x622d3d str pos: 0x62308f length: 17
avastemupdate.exe

key pos: 0x61d297 str pos: 0x61d207 length: 12
unsecapp.exe

key pos: 0x61e17f str pos: 0x61dd2f length: 12
avgamsvr.exe

key pos: 0x619870 str pos: 0x619774 length: 9
avgas.exe

key pos: 0x61c302 str pos: 0x61bae3 length: 11
avgcc32.exe

key pos: 0x619168 str pos: 0x6192b5 length: 9
avgcc.exe

key pos: 0x61c226 str pos: 0x61b9ba length: 11
avgctrl.exe

key pos: 0x61c13f str pos: 0x61be74 length: 11
avgdiag.exe

key pos: 0x61a4c2 str pos: 0x61aad0 length: 10
avgemc.exe

key pos: 0x61bb46 str pos: 0x61c386 length: 11
avgfws8.exe

key pos: 0x61d42f str pos: 0x61e8db length: 12
avgfwsrv.exe

key pos: 0x61ba54 str pos: 0x61c294 length: 11
avginet.exe

key pos: 0x61bd35 str pos: 0x61c906 length: 11
avgmsvr.exe

key pos: 0x61e1d3 str pos: 0x61dd53 length: 12
avgrssvc.exe

key pos: 0x61df33 str pos: 0x61ee7b length: 12
avgscanx.exe

key pos: 0x61e437 str pos: 0x61d78f length: 12
avgserv9.exe

key pos: 0x61c29f str pos: 0x61ba49 length: 11
avgserv.exe

key pos: 0x61ac88 str pos: 0x619f7c length: 10
avgupd.exe

key pos: 0x61edbb str pos: 0x61d6f3 length: 12
avgupdln.exe

key pos: 0x61e33b str pos: 0x61dfb7 length: 12
avgupsvc.exe

key pos: 0x619beb str pos: 0x61958e length: 9
avgvv.exe

key pos: 0x61993f str pos: 0x6195fa length: 9
avgwb.dat

key pos: 0x618b70 str pos: 0x618a00 length: 8
avgw.exe

key pos: 0x61d45f str pos: 0x61e8c3 length: 12
avgwizfw.exe

key pos: 0x6195e8 str pos: 0x619c2a length: 9
guard.exe

key pos: 0x61e527 str pos: 0x61d8bb length: 12
avgcsrvx.exe

key pos: 0x6214b3 str pos: 0x621963 length: 15
avgidsagent.exe

key pos: 0x622f19 str pos: 0x622f5d length: 17
avgidsmonitor.exe

key pos: 0x61e683 str pos: 0x61da47 length: 12
avgidsui.exe

key pos: 0x622df8 str pos: 0x623403 length: 17
avgidswatcher.exe

key pos: 0x619747 str pos: 0x619882 length: 9
avgam.exe

key pos: 0x61a68e str pos: 0x61ac4c length: 10
avgnsx.exe

key pos: 0x61bac2 str pos: 0x61c318 length: 11
avgfws9.exe

key pos: 0x61a206 str pos: 0x619f40 length: 10
avgrsx.exe

key pos: 0x61c8f0 str pos: 0x61bcbc length: 11
avgtray.exe

key pos: 0x61e827 str pos: 0x61dbf7 length: 12
avgwdsvc.exe

key pos: 0x61c6a9 str pos: 0x61b8c8 length: 11
sidebar.exe

key pos: 0x61cdf3 str pos: 0x61ca57 length: 12
avgchsvx.exe

key pos: 0x61c91c str pos: 0x61be48 length: 11
avgcmgr.exe

key pos: 0x61ba5f str pos: 0x61c2b5 length: 11
avgemcx.exe

key pos: 0x61a49a str pos: 0x61aabc length: 10
avgfws.exe

key pos: 0x61e6a7 str pos: 0x61da77 length: 12
avgmfapx.exe

key pos: 0x620325 str pos: 0x61ffdd length: 14
avgcefrend.exe

key pos: 0x61e51b str pos: 0x61d903 length: 12
avgcsrva.exe

key pos: 0x61b122 str pos: 0x61b445 length: 11
avgemca.exe

key pos: 0x61ac38 str pos: 0x61a698 length: 10
avgnsa.exe

key pos: 0x61a2ec str pos: 0x61ada0 length: 10
avgrsa.exe

key pos: 0x622dd6 str pos: 0x622fe5 length: 17
loggingserver.exe

key pos: 0x623b2e str pos: 0x62397e length: 18
toolbarupdater.exe

key pos: 0x6245ec str pos: 0x6247c7 length: 19
wtusystemsuport.exe

key pos: 0x61ce23 str pos: 0x61d2a3 length: 12
avgregcl.exe

key pos: 0x61ca7b str pos: 0x61cdff length: 12
avgsystx.exe

key pos: 0x619510 str pos: 0x619c60 length: 9
vprot.exe

key pos: 0x61cb3b str pos: 0x61cfd3 length: 12
avcenter.exe

key pos: 0x61d0ab str pos: 0x61cc37 length: 12
avconfig.exe

key pos: 0x619dec str pos: 0x61a06c length: 10
avesvc.exe

key pos: 0x61c507 str pos: 0x61b794 length: 11
avmailc.exe

key pos: 0x61c0c6 str pos: 0x61bd6c length: 11
avmcdlg.exe

key pos: 0x61d027 str pos: 0x61cbcb length: 12
avnotify.exe

key pos: 0x61a79c str pos: 0x61a99a length: 10
avscan.exe

key pos: 0x61df6f str pos: 0x61e3b3 length: 12
guardgui.exe

key pos: 0x61b0f6 str pos: 0x61b3cc length: 11
avadmin.exe

key pos: 0x61b66b str pos: 0x61b298 length: 11
avfwsvc.exe

key pos: 0x61eac7 str pos: 0x61d31b length: 12
avwebgrd.exe

key pos: 0x619cfc str pos: 0x61a012 length: 10
fwinst.exe

key pos: 0x6244f5 str pos: 0x62490a length: 19
sysoptenginesvc.exe

key pos: 0x61b608 str pos: 0x61b214 length: 11
bavtray.exe

key pos: 0x61e713 str pos: 0x61db37 length: 12
bhipssvc.exe

key pos: 0x618ad0 str pos: 0x6189d0 length: 8
bmrt.exe

key pos: 0x61f5d0 str pos: 0x61f92a length: 13
seccenter.exe

key pos: 0x61bca6 str pos: 0x61bfa8 length: 11
gziface.exe

key pos: 0x61a0b2 str pos: 0x619e64 length: 10
gzserv.exe

key pos: 0x6186b2 str pos: 0x6187c3 length: 7
bdc.exe

key pos: 0x61a3f0 str pos: 0x61aea4 length: 10
bdlite.exe

key pos: 0x619de2 str pos: 0x61a044 length: 10
bdmcon.exe

key pos: 0x61d7d7 str pos: 0x61e3d7 length: 12
bdsubmit.exe

key pos: 0x61fed3 str pos: 0x6201c7 length: 14
deloeminfs.exe

key pos: 0x61c44c str pos: 0x61bab7 length: 11
livesrv.exe

key pos: 0x622230 str pos: 0x6228b0 length: 16
setloadorder.exe

key pos: 0x619fcc str pos: 0x619ec8 length: 10
vsserv.exe

key pos: 0x61e21b str pos: 0x61dea3 length: 12
xcommsvr.exe

key pos: 0x618761 str pos: 0x6186f8 length: 7
bka.exe

key pos: 0x6251dc str pos: 0x6258e4 length: 20
bkavsystemserver.exe

key pos: 0x619f04 str pos: 0x61a210 length: 10
blupro.exe

key pos: 0x61a7c4 str pos: 0x61a9fe length: 10
blackd.exe

key pos: 0x61d267 str pos: 0x61cd33 length: 12
blackice.exe

key pos: 0x61becc str pos: 0x61c058 length: 11
proutil.exe

key pos: 0x61a2b0 str pos: 0x619e8c length: 10
rapapp.exe

key pos: 0x61be7f str pos: 0x61c16b length: 11
basfipm.exe

key pos: 0x61956a str pos: 0x619c33 length: 9
isafe.exe

key pos: 0x61a30a str pos: 0x61adb4 length: 10
cavrid.exe

key pos: 0x61aaee str pos: 0x61a5da length: 10
vetmsg.exe

key pos: 0x618ef8 str pos: 0x618d38 length: 8
amswmagt

key pos: 0x618959 str pos: 0x618696 length: 7
caf.exe

key pos: 0x6188bf str pos: 0x6185ee length: 7
capmuam

key pos: 0x6186ff str pos: 0x61876f length: 7
agt.exe

key pos: 0x61f8f6 str pos: 0x61f4d9 length: 13
ccnfagent.exe

key pos: 0x61d90f str pos: 0x61e4af length: 12
ccsmagtd.exe

key pos: 0x6209b5 str pos: 0x620555 length: 14
cfftplugin.exe

key pos: 0x61fd47 str pos: 0x61f4a5 length: 13
cfnotsrvd.exe

key pos: 0x61c69e str pos: 0x61b697 length: 11
cfsmsmd.exe

key pos: 0x61972c str pos: 0x619867 length: 9
alert.exe

key pos: 0x61d72f str pos: 0x61ecfb length: 12
igateway.exe

key pos: 0x61b7cb str pos: 0x61c6e0 length: 11
inotask.exe

key pos: 0x62336a str pos: 0x622da3 length: 17
caantispyware.exe

key pos: 0x621d32 str pos: 0x62170b length: 15
caavcmdscan.exe

key pos: 0x618f38 str pos: 0x618d98 length: 8
caav.exe

key pos: 0x6217fb str pos: 0x6216c0 length: 15
caavguiscan.exe

key pos: 0x618f98 str pos: 0x618cf8 length: 8
cafw.exe

key pos: 0x61fd95 str pos: 0x61f708 length: 13
calogdump.exe

key pos: 0x61bbca str pos: 0x61c48e length: 11
capfaem.exe

key pos: 0x61b1d2 str pos: 0x61b584 length: 11
capfsem.exe

key pos: 0x627ca6 str pos: 0x627b3e length: 24
cappactiveprotection.exe

key pos: 0x624f0c str pos: 0x62563c length: 20
casecuritycenter.exe

key pos: 0x61a9ea str pos: 0x61a828 length: 10
caunst.exe

key pos: 0x61a724 str pos: 0x61af6c length: 10
cavrep.exe

key pos: 0x61af9e str pos: 0x61a7f6 length: 10
cctray.exe

key pos: 0x61e0fb str pos: 0x61dce7 length: 12
ccupdate.exe

key pos: 0x61ce77 str pos: 0x61cc1f length: 12
isafinst.exe

key pos: 0x629dcd str pos: 0x629fc5 length: 28
itmrt_supportdiagnostics.exe

key pos: 0x61e80f str pos: 0x61dafb length: 12
itmrtsvc.exe

key pos: 0x621837 str pos: 0x621675 length: 15
itmrt_trace.exe

key pos: 0x61bc9b str pos: 0x61c181 length: 11
ppclean.exe

key pos: 0x61d81f str pos: 0x61e71f length: 12
umxagent.exe

key pos: 0x61a29c str pos: 0x619e96 length: 10
umxcfg.exe

key pos: 0x61ee3f str pos: 0x61df3f length: 12
umxfwhlp.exe

key pos: 0x61a350 str pos: 0x61ae86 length: 10
umxpol.exe

key pos: 0x61ba1d str pos: 0x61c478 length: 11
unvet32.exe

key pos: 0x61eb9f str pos: 0x61d537 length: 12
capfasem.exe

key pos: 0x61d30f str pos: 0x61eb4b length: 12
ccprovsp.exe

key pos: 0x61f36d str pos: 0x61fc02 length: 13
ppctlpriv.exe

key pos: 0x618f78 str pos: 0x618ce8 length: 8
casc.exe

key pos: 0x6238ca str pos: 0x623b88 length: 18
ccschedulersvc.exe

key pos: 0x623912 str pos: 0x623f78 length: 18
ccsystemreport.exe

key pos: 0x61e59f str pos: 0x61d7a7 length: 12
inonmsrv.exe

key pos: 0x61a9a4 str pos: 0x61a6d4 length: 10
inoweb.exe

key pos: 0x61f51a str pos: 0x61f91d length: 13
auth8021x.exe

key pos: 0x61cd3f str pos: 0x61d0e7 length: 12
krbcc32s.exe

key pos: 0x618809 str pos: 0x6183cc length: 7
pep.exe

key pos: 0x61beb6 str pos: 0x61c8c4 length: 11
realmon.exe

key pos: 0x61d1e3 str pos: 0x61ca93 length: 12
repmgr64.exe

key pos: 0x61ff97 str pos: 0x62027d length: 14
csacontrol.exe

key pos: 0x61f9c6 str pos: 0x61f65f length: 13
leventmgr.exe

key pos: 0x61cf67 str pos: 0x61cac3 length: 12
okclient.exe

key pos: 0x61d60f str pos: 0x61ecef length: 12
clamscan.exe

key pos: 0x61e593 str pos: 0x61d9b7 length: 12
clamtray.exe

key pos: 0x61c4af str pos: 0x61bbbf length: 11
clamwin.exe

key pos: 0x61ed8b str pos: 0x61d69f length: 12
ccemflsv.exe

key pos: 0x61b92b str pos: 0x61b768 length: 11
cssauth.exe

key pos: 0x61bc90 str pos: 0x61c042 length: 11
cavscan.exe

key pos: 0x618dd0 str pos: 0x618e70 length: 8
clps.exe

key pos: 0x61a2c4 str pos: 0x61ad8c length: 10
clpsla.exe

key pos: 0x61a814 str pos: 0x61a9e0 length: 10
clpsls.exe

key pos: 0x62049f str pos: 0x620d97 length: 14
cmdinstall.exe

key pos: 0x61f5dd str pos: 0x61fa3b length: 13
cfpconfig.exe

key pos: 0x61893d str pos: 0x61870d length: 7
cfp.exe

key pos: 0x61e5ff str pos: 0x61d9ff length: 12
cfplogvw.exe

key pos: 0x61deeb str pos: 0x61e2db length: 12
cfpsbmit.exe

key pos: 0x61cc07 str pos: 0x61d00f length: 12
cfpupdat.exe

key pos: 0x61d597 str pos: 0x61eb6f length: 12
crashrep.exe

key pos: 0x61875a str pos: 0x6186ea length: 7
cpf.exe

key pos: 0x61e953 str pos: 0x61d46b length: 12
cfpconfg.exe

key pos: 0x624424 str pos: 0x624ae5 length: 19
csfalconservice.exe

key pos: 0x61f3c8 str pos: 0x61fb0b length: 13
cylanceui.exe

key pos: 0x6202ed str pos: 0x61ffcf length: 14
cylancesvc.exe

key pos: 0x61d21f str pos: 0x61cd63 length: 12
cramtray.exe

key pos: 0x61a42c str pos: 0x61aee0 length: 10
crssvc.exe

key pos: 0x619711 str pos: 0x61984c length: 9
amsvc.exe

key pos: 0x6202c3 str pos: 0x61ff51 length: 14
frzstate2k.exe

key pos: 0x61e96b str pos: 0x61d507 length: 12
drwagnui.exe

key pos: 0x61c67d str pos: 0x61b82e length: 11
drweb32.exe

key pos: 0x61e2ab str pos: 0x61debb length: 12
drweb32w.exe

key pos: 0x61deaf str pos: 0x61e27b length: 12
drweb386.exe

key pos: 0x61e5cf str pos: 0x61d93f length: 12
drwebcgp.exe

key pos: 0x61b256 str pos: 0x61c4db length: 11
drwebdc.exe

key pos: 0x619597 str pos: 0x619bac length: 9
drweb.exe

key pos: 0x61db4f str pos: 0x61e81b length: 12
drwebmng.exe

key pos: 0x61cfc7 str pos: 0x61cc13 length: 12
drwebscd.exe

key pos: 0x61da6b str pos: 0x61e72b length: 12
drwebupw.exe

key pos: 0x61d603 str pos: 0x61ece3 length: 12
drwebwcl.exe

key pos: 0x61e347 str pos: 0x61e023 length: 12
drwebwin.exe

key pos: 0x61bbb4 str pos: 0x61c3c8 length: 11
drwinst.exe

key pos: 0x61ddcb str pos: 0x61e38f length: 12
spiderml.exe

key pos: 0x61e6bf str pos: 0x61d91b length: 12
spidernt.exe

key pos: 0x61e167 str pos: 0x61df87 length: 12
spiderui.exe

key pos: 0x61d0f3 str pos: 0x61ccc7 length: 12
drwagntd.exe

key pos: 0x620317 str pos: 0x620015 length: 14
drwupgrade.exe

key pos: 0x61cff7 str pos: 0x61cae7 length: 12
drwebcom.exe

key pos: 0x61e47f str pos: 0x61d8eb length: 12
eeyeevnt.exe

key pos: 0x621fa0 str pos: 0x621ea0 length: 16
retinaengine.exe

key pos: 0x61b138 str pos: 0x61b47c length: 11
a2guard.exe

key pos: 0x61bd14 str pos: 0x61c09a length: 11
a2start.exe

key pos: 0x622b1d str pos: 0x622930 length: 17
administrator.exe

key pos: 0x62303a str pos: 0x622e80 length: 17
control_panel.exe

key pos: 0x61e95f str pos: 0x61d663 length: 12
usergate.exe

key pos: 0x61e4d3 str pos: 0x61d79b length: 12
esmagent.exe

key pos: 0x6185af str pos: 0x6183e1 length: 7
era.exe

key pos: 0x6268d0 str pos: 0x626ea8 length: 22
ppmcativedetection.exe

key pos: 0x61c7fe str pos: 0x61b839 length: 11
vettray.exe

key pos: 0x61b21f str pos: 0x61b629 length: 11
cavtray.exe

key pos: 0x61a832 str pos: 0x61aa4e length: 10
inorpc.exe

key pos: 0x619c18 str pos: 0x61954f length: 9
inort.exe

key pos: 0x618302 str pos: 0x6181e8 length: 6
ca.exe

key pos: 0x61c344 str pos: 0x61bad8 length: 11
caissdt.exe

key pos: 0x61b2a3 str pos: 0x61b5e7 length: 11
etagent.exe

key pos: 0x622d1b str pos: 0x622b94 length: 17
etloganalyzer.exe

key pos: 0x620627 str pos: 0x6209fb length: 14
etrssfeeds.exe

key pos: 0x61cb6b str pos: 0x61d057 length: 12
evtarmgr.exe

key pos: 0x61a558 str pos: 0x61ab3e length: 10
evtmgr.exe

key pos: 0x620a33 str pos: 0x6205ef length: 14
etreporter.exe

key pos: 0x62066d str pos: 0x6207bd length: 14
etconsole3.exe

key pos: 0x62491d str pos: 0x62458d length: 19
etwcontrolpanel.exe

key pos: 0x622360 str pos: 0x622570 length: 16
useranalysis.exe

key pos: 0x61d3ff str pos: 0x61ebab length: 12
etcorrel.exe

key pos: 0x625128 str pos: 0x624ed0 length: 20
evtprocessecfile.exe

key pos: 0x6214c2 str pos: 0x621936 length: 15
etscheduler.exe

key pos: 0x621eb0 str pos: 0x621fb0 length: 16
useractivity.exe

key pos: 0x623f66 str pos: 0x6239c6 length: 18
traptrackermgr.exe

key pos: 0x61fd88 str pos: 0x61f6d4 length: 13
ewidoctrl.exe

key pos: 0x620309 str pos: 0x62004d length: 14
ewidoguard.exe

key pos: 0x627e0e str pos: 0x6281e6 length: 24
nslocollectorservice.exe

key pos: 0x618d88 str pos: 0x618f28 length: 8
fmon.exe

key pos: 0x61b0b4 str pos: 0x61b31c length: 11
fortifw.exe

key pos: 0x621acb str pos: 0x62130f length: 15
update_task.exe

key pos: 0x6200a1 str pos: 0x61feb7 length: 14
fpavserver.exe

key pos: 0x61f72f str pos: 0x61f80c length: 13
fprottray.exe

key pos: 0x61bb5c str pos: 0x61c4c5 length: 11
fameh32.exe

key pos: 0x619a3b str pos: 0x61929a length: 9
fspex.exe

key pos: 0x618d20 str pos: 0x6190a8 length: 8
fsaa.exe

key pos: 0x618a90 str pos: 0x618c90 length: 8
bwgo0000

key pos: 0x6195a0 str pos: 0x619b64 length: 9
fch32.exe

key pos: 0x6196db str pos: 0x619a32 length: 9
fih32.exe

key pos: 0x619750 str pos: 0x619843 length: 9
fsaua.exe

key pos: 0x61a9ae str pos: 0x61a756 length: 10
fsav32.exe

key pos: 0x61a300 str pos: 0x61ad6e length: 10
fscuif.exe

key pos: 0x61a7ba str pos: 0x61a95e length: 10
fsdfwd.exe

key pos: 0x61ade6 str pos: 0x61a40e length: 10
fsgk32.exe

key pos: 0x61dc93 str pos: 0x61e0e3 length: 12
fsgk32st.exe

key pos: 0x61d5f7 str pos: 0x61ed07 length: 12
fsguidll.exe

key pos: 0x61d16b str pos: 0x61cc4f length: 12
fsguiexe.exe

key pos: 0x61d58b str pos: 0x61eabb length: 12
fshdll32.exe

key pos: 0x619558 str pos: 0x619c06 length: 9
fsm32.exe

key pos: 0x619eb4 str pos: 0x61a1b6 length: 10
fsma32.exe

key pos: 0x61a9b8 str pos: 0x61a710 length: 10
fsmb32.exe

key pos: 0x61a80a str pos: 0x61afa8 length: 10
fsorsp.exe

key pos: 0x618dc8 str pos: 0x618e60 length: 8
fspc.exe

key pos: 0x6189e0 str pos: 0x618ae0 length: 8
fsqh.exe

key pos: 0x61afb2 str pos: 0x61a7ce length: 10
fssm32.exe

key pos: 0x622190 str pos: 0x6228e0 length: 16
setupguimngr.exe

key pos: 0x61b1b1 str pos: 0x61b3b6 length: 11
tnbutil.exe

key pos: 0x61c86c str pos: 0x61b936 length: 11
fsavgui.exe

key pos: 0x61a62a str pos: 0x61ab66 length: 10
gdscan.exe

key pos: 0x61eb33 str pos: 0x61d36f length: 12
avkproxy.exe

key pos: 0x6200d9 str pos: 0x620341 length: 14
avkservice.exe

key pos: 0x61b891 str pos: 0x61c759 length: 11
avktray.exe

key pos: 0x61c8cf str pos: 0x61bc6f length: 11
avkwctl.exe

key pos: 0x6238b8 str pos: 0x623b64 length: 18
gdfirewalltray.exe

key pos: 0x61b5f2 str pos: 0x61b2ae length: 11
gdfwsvc.exe

key pos: 0x625114 str pos: 0x624e94 length: 20
endpointsecurity.exe

key pos: 0x62123d str pos: 0x62103f length: 15
esecservice.exe

key pos: 0x6268e6 str pos: 0x626f58 length: 22
gfireporterservice.exe

key pos: 0x624768 str pos: 0x624671 length: 19
esecagntservice.exe

key pos: 0x61e533 str pos: 0x61db07 length: 12
rcsvcmon.exe

key pos: 0x620f04 str pos: 0x6211a7 length: 15
dolphincharge.e

key pos: 0x622ad9 str pos: 0x622d0a length: 17
dolphincharge.exe

key pos: 0x61ca87 str pos: 0x61d063 length: 12
loggetor.exe

key pos: 0x623c3c str pos: 0x623786 length: 18
netalertclient.exe

key pos: 0x621657 str pos: 0x621747 length: 15
printdevice.exe

key pos: 0x621d41 str pos: 0x6214ef length: 15
pwdfilthelp.exe

key pos: 0x61d75f str pos: 0x61ebb7 length: 12
pthosttr.exe

key pos: 0x61e18b str pos: 0x61dc6f length: 12
hpqwmiex.exe

key pos: 0x61f910 str pos: 0x61f54e length: 13
ntcaagent.exe

key pos: 0x6209a7 str pos: 0x6204c9 length: 14
ntcadaemon.exe

key pos: 0x621495 str pos: 0x6218af length: 15
ntcaservice.exe

key pos: 0x625dec str pos: 0x62654e length: 21
privacyiconclient.exe

key pos: 0x61dd0b str pos: 0x61e2cf length: 12
rapuisvc.exe

key pos: 0x61a922 str pos: 0x61a7d8 length: 10
vpatch.exe

key pos: 0x61b185 str pos: 0x61b35e length: 11
tclproc.exe

key pos: 0x61a332 str pos: 0x61acba length: 10
isscsf.exe

key pos: 0x61f0f0 str pos: 0x61f2d1 length: 13
issdaemon.exe

key pos: 0x61e677 str pos: 0x61dbbb length: 12
kvdetech.exe

key pos: 0x61fd20 str pos: 0x61f457 length: 13
kvmonxp_2.kxp

key pos: 0x61c3d3 str pos: 0x61bb04 length: 11
kvmonxp.kxp

key pos: 0x61cd57 str pos: 0x61d0b7 length: 12
kvolself.exe

key pos: 0x61f20e str pos: 0x61efab length: 13
kvsrvxp_1.exe

key pos: 0x61c1ef str pos: 0x61be69 length: 11
kvsrvxp.exe

key pos: 0x618a80 str pos: 0x618c48 length: 8
kvxp.kxp

key pos: 0x621c8d str pos: 0x62124c length: 15
ppppwallrun.exe

key pos: 0x619798 str pos: 0x6198ca length: 9
avpcc.exe

key pos: 0x61c252 str pos: 0x61ba12 length: 11
avpexec.exe

key pos: 0x618a78 str pos: 0x618c98 length: 8
avpm.exe

key pos: 0x61af62 str pos: 0x61a6de length: 10
avpncc.exe

key pos: 0x618df8 str pos: 0x618e88 length: 8
avps.exe

key pos: 0x61adaa str pos: 0x61a3b4 length: 10
avpupd.exe

key pos: 0x6188c6 str pos: 0x618618 length: 7
kav.exe

key pos: 0x61e557 str pos: 0x61d82b length: 12
kavisarv.exe

key pos: 0x61981f str pos: 0x6198e5 length: 9
kavmm.exe

key pos: 0x6199b4 str pos: 0x619639 length: 9
kavss.exe

key pos: 0x61a620 str pos: 0x61ac42 length: 10
kavsvc.exe

key pos: 0x6188b8 str pos: 0x618626 length: 7
kis.exe

key pos: 0x61cb9b str pos: 0x61cecb length: 12
klnagent.exe

key pos: 0x619c3c str pos: 0x6195a9 length: 9
klswd.exe

key pos: 0x61dcf3 str pos: 0x61e227 length: 12
klwtblfs.exe

key pos: 0x61b537 str pos: 0x61b22a length: 11
kwsprod.exe

key pos: 0x61c021 str pos: 0x61bdfb length: 11
up2date.exe

key pos: 0x61e69b str pos: 0x61db5b length: 12
klserver.exe

key pos: 0x62035d str pos: 0x61ff6d length: 14
oespamtest.exe

key pos: 0x622d70 str pos: 0x6230c2 length: 17
kavadapterexe.exe

key pos: 0x62472f str pos: 0x624638 length: 19
kavlotsingleton.exe

key pos: 0x61c7b1 str pos: 0x61b96d length: 11
kavfsgt.exe

key pos: 0x61e653 str pos: 0x61dba3 length: 12
kavfsrcn.exe

key pos: 0x6198f7 str pos: 0x619816 length: 9
kavfs.exe

key pos: 0x61b1e8 str pos: 0x61c4d0 length: 11
kavfswp.exe

key pos: 0x61e87b str pos: 0x61cc67 length: 12
kavshell.exe

key pos: 0x6218be str pos: 0x62144a length: 15
klnacserver.exe

key pos: 0x61e9fb str pos: 0x61d4bf length: 12
avpdtagt.exe

key pos: 0x61ad3c str pos: 0x61a3a0 length: 10
netcfg.exe

key pos: 0x61e78b str pos: 0x61dab3 length: 12
kavfsscs.exe

key pos: 0x61bc85 str pos: 0x61c911 length: 11
kavtray.exe

key pos: 0x619e78 str pos: 0x61ac6a length: 10
persfw.exe

key pos: 0x61daa7 str pos: 0x61e68f length: 12
avserver.exe

key pos: 0x61e467 str pos: 0x61daef length: 12
winroute.exe

key pos: 0x61a60c str pos: 0x61aaa8 length: 10
wrctrl.exe

key pos: 0x621da0 str pos: 0x622010 length: 16
kabackreport.exe

key pos: 0x61c32e str pos: 0x61bb51 length: 11
kaccore.exe

key pos: 0x61f7e5 str pos: 0x61f6fb length: 13
kanmcmain.exe

key pos: 0x61b369 str pos: 0x61b159 length: 11
kastray.exe

key pos: 0x61b2da str pos: 0x61b56e length: 11
kislive.exe

key pos: 0x61e2ff str pos: 0x61e02f length: 12
kmailmon.exe

key pos: 0x6224a0 str pos: 0x622400 length: 16
knupdatemain.exe

key pos: 0x6215c1 str pos: 0x6217bf length: 15
kswebshield.exe

key pos: 0x61c93d str pos: 0x61bf92 length: 11
kxeserv.exe

key pos: 0x61a3aa str pos: 0x61aefe length: 10
uplive.exe

key pos: 0x61b8de str pos: 0x61c72d length: 11
kansgui.exe

key pos: 0x619e82 str pos: 0x619ff4 length: 10
kansvr.exe

key pos: 0x61da3b str pos: 0x61e7c7 length: 12
kavstart.exe

key pos: 0x61be1c str pos: 0x61c197 length: 11
kpfwsvc.exe

key pos: 0x61a530 str pos: 0x61afda length: 10
kwatch.exe

key pos: 0x6199cf str pos: 0x61961e length: 9
kav32.exe

key pos: 0x61a486 str pos: 0x61ab16 length: 10
kissvc.exe

key pos: 0x61a846 str pos: 0x61aa58 length: 10
kpfw32.exe

key pos: 0x61aa76 str pos: 0x61a792 length: 10
system.exe

key pos: 0x61d6cf str pos: 0x61eb57 length: 12
wssfcmai.exe

key pos: 0x620e15 str pos: 0x62051d length: 14
aawservice.exe

key pos: 0x622200 str pos: 0x6226f0 length: 16
ad-aware2007.exe

key pos: 0x619ca8 str pos: 0x619804 length: 9
nlsvc.exe

key pos: 0x621fc0 str pos: 0x621de0 length: 16
engineserver.exe

key pos: 0x62135a str pos: 0x621c33 length: 15
eventparser.exe

key pos: 0x61f0fd str pos: 0x61f24f length: 13
log_qtine.exe

key pos: 0x61a7ec str pos: 0x61afc6 length: 10
mfeann.exe

key pos: 0x61ddb3 str pos: 0x61e077 length: 12
nailgpip.exe

key pos: 0x61b9f1 str pos: 0x61c3bd length: 11
rpcserv.exe

key pos: 0x619dce str pos: 0x61a1de length: 10
srvmon.exe

key pos: 0x61c4a4 str pos: 0x61baf9 length: 11
mcagent.exe

key pos: 0x61d33f str pos: 0x61e947 length: 12
mfemactl.exe

key pos: 0x61ce5f str pos: 0x61cadb length: 12
macmnsvc.exe

key pos: 0x619264 str pos: 0x6194c8 length: 9
masvc.exe

key pos: 0x61df1b str pos: 0x61e2e7 length: 12
masalert.exe

key pos: 0x61a940 str pos: 0x61a738 length: 10
msssrv.exe

key pos: 0x61a6fc str pos: 0x61a972 length: 10
massrv.exe

key pos: 0x61a2ba str pos: 0x61ad64 length: 10
msscli.exe

key pos: 0x61d1ef str pos: 0x61cd7b length: 12
mcshld9x.exe

key pos: 0x61ee87 str pos: 0x61df03 length: 12
mgavrtcl.exe

key pos: 0x61d70b str pos: 0x61ec17 length: 12
mcappins.exe

key pos: 0x61f312 str pos: 0x61f095 length: 13
mfecanary.exe

key pos: 0x621c24 str pos: 0x6213e1 length: 15
macompatsvc.exe

key pos: 0x61bb67 str pos: 0x61c37b length: 11
mcvsrte.exe

key pos: 0x61c693 str pos: 0x61b681 length: 11
mfefire.exe

key pos: 0x61c30d str pos: 0x61bb25 length: 11
dao_log.exe

key pos: 0x61b9a4 str pos: 0x61c273 length: 11
firesvc.exe

key pos: 0x61e7f7 str pos: 0x61dbc7 length: 12
firetray.exe

key pos: 0x61adf0 str pos: 0x61a44a length: 10
mfeesp.exe

key pos: 0x61d51f str pos: 0x61ea8b length: 12
naprdmgr.exe

key pos: 0x6185d9 str pos: 0x61843c length: 7
cpd.exe

key pos: 0x6197b3 str pos: 0x61985e length: 9
mfefw.exe

key pos: 0x6216de str pos: 0x621864 length: 15
frameworkservic

key pos: 0x61d5eb str pos: 0x61ec47 length: 12
cmgrdian.exe

key pos: 0x61b542 str pos: 0x61b2c4 length: 11
mcshell.exe

key pos: 0x61a652 str pos: 0x61abf2 length: 10
mfehcs.exe

key pos: 0x61ab20 str pos: 0x61a4e0 length: 10
mcinfo.exe

key pos: 0x6196ff str pos: 0x6199fc length: 9
hwapi.exe

key pos: 0x625308 str pos: 0x625614 length: 20
mcafeedatabackup.exe

key pos: 0x61d6e7 str pos: 0x61ec2f length: 12
mcmscsvc.exe

key pos: 0x61baee str pos: 0x61c436 length: 11
mcnasvc.exe

key pos: 0x61997e str pos: 0x61964b length: 9
mcods.exe

key pos: 0x61cb23 str pos: 0x61ce53 length: 12
mcpromgr.exe

key pos: 0x61bde5 str pos: 0x61c1ce length: 11
mcproxy.exe

key pos: 0x61bf24 str pos: 0x61c176 length: 11
mcuimgr.exe

key pos: 0x61a468 str pos: 0x61addc length: 10
mpfsrv.exe

key pos: 0x619e1e str pos: 0x619ffe length: 10
mpsevh.exe

key pos: 0x61849e str pos: 0x6183a2 length: 7
mps.exe

key pos: 0x61cc73 str pos: 0x61d22b length: 12
msksrver.exe

key pos: 0x61dc87 str pos: 0x61e263 length: 12
redirsvc.exe

key pos: 0x61f158 str pos: 0x61f0a2 length: 13
saservice.exe

key pos: 0x61bb7d str pos: 0x61c289 length: 11
siteadv.exe

key pos: 0x619e32 str pos: 0x619fc2 length: 10
mfemms.exe

key pos: 0x61cab7 str pos: 0x61cfeb length: 12
neotrace.exe

key pos: 0x61cbd7 str pos: 0x61d25b length: 12
vshwin32.exe

key pos: 0x61d8af str pos: 0x61e5b7 length: 12
mpfagent.exe

key pos: 0x61ff0b str pos: 0x620085 length: 14
mpfconsole.exe

key pos: 0x618649 str pos: 0x61891a length: 7
mpf.exe

key pos: 0x62098b str pos: 0x6204e5 length: 14
mpfservice.exe

key pos: 0x61c1d9 str pos: 0x61bdf0 length: 11
mpftray.exe

key pos: 0x61cfa3 str pos: 0x61cacf length: 12
mscifapp.exe

key pos: 0x61bd8d str pos: 0x61bfbe length: 11
mfevtps.exe

key pos: 0x61a436 str pos: 0x61ad82 length: 10
qclean.exe

key pos: 0x61ebff str pos: 0x61d723 length: 12
mcregwiz.exe

key pos: 0x61dacb str pos: 0x61e42b length: 12
rssensor.exe

key pos: 0x6216fc str pos: 0x6217ce length: 15
safeservice.exe

key pos: 0x61dc3f str pos: 0x61e257 length: 12
ncdaemon.exe

key pos: 0x61a5a8 str pos: 0x61aa9e length: 10
mcdash.exe

key pos: 0x61d97b str pos: 0x61eeab length: 12
mcdetect.exe

key pos: 0x621765 str pos: 0x6216b1 length: 15
ssscheduler.exe

key pos: 0x620a79 str pos: 0x620405 length: 14
sahookmain.exe

key pos: 0x61dc4b str pos: 0x61e20f length: 12
mskdetct.exe

key pos: 0x61c23c str pos: 0x61baa1 length: 11
msksrvr.exe

key pos: 0x61ddbf str pos: 0x61e0cb length: 12
mskagent.exe

key pos: 0x61c323 str pos: 0x61b983 length: 11
stinger.exe

key pos: 0x61de7f str pos: 0x61e35f length: 12
mcsysmon.exe

key pos: 0x61e48b str pos: 0x61d957 length: 12
mctskshd.exe

key pos: 0x6198a6 str pos: 0x61971a length: 9
mfetp.exe

key pos: 0x61db2b str pos: 0x61e7d3 length: 12
myagttry.exe

key pos: 0x61ee03 str pos: 0x61dde3 length: 12
mcupdmgr.exe

key pos: 0x61d39f str pos: 0x61eda3 length: 12
rulaunch.exe

key pos: 0x61e0ef str pos: 0x61dd3b length: 12
mcvsshld.exe

key pos: 0x6199bd str pos: 0x6196d2 length: 9
tbmon.exe

key pos: 0x61e12b str pos: 0x61dcff length: 12
alogserv.exe

key pos: 0x61d867 str pos: 0x61e587 length: 12
mcmnhdlr.exe

key pos: 0x61aada str pos: 0x61a526 length: 10
mghtml.exe

key pos: 0x619561 str pos: 0x619bd0 length: 9
edisk.exe

key pos: 0x619e46 str pos: 0x61a1fc length: 10
scan32.exe

key pos: 0x625600 str pos: 0x62536c length: 20
frameworkservice.exe

key pos: 0x61d24f str pos: 0x61ccbb length: 12
mcconsol.exe

key pos: 0x6237bc str pos: 0x623d6e length: 18
mcscript_inuse.exe

key pos: 0x61a8be str pos: 0x61a788 length: 10
mctray.exe

key pos: 0x61dc27 str pos: 0x61d2bb length: 12
mcupdate.exe

key pos: 0x61a094 str pos: 0x619f2c length: 10
shstat.exe

key pos: 0x61d49b str pos: 0x61ecd7 length: 12
udaterui.exe

key pos: 0x61f4e6 str pos: 0x61fa2e length: 13
updaterui.exe

key pos: 0x61af58 str pos: 0x61a7a6 length: 10
mcepoc.exe

key pos: 0x61cc2b str pos: 0x61ce0b length: 12
mcepocfg.exe

key pos: 0x61fa07 str pos: 0x61f611 length: 13
mcpalmcfg.exe

key pos: 0x61e83f str pos: 0x61da9b length: 12
mcwcecfg.exe

key pos: 0x619cba str pos: 0x6197e0 length: 9
mcwce.exe

key pos: 0x62478e str pos: 0x62464b length: 19
frameworkservic.exe

key pos: 0x61a86e str pos: 0x61a990 length: 10
vsmain.exe

key pos: 0x61c2c0 str pos: 0x61ba07 length: 11
oasclnt.exe

key pos: 0x61aa6c str pos: 0x61a71a length: 10
vsstat.exe

key pos: 0x61e2c3 str pos: 0x61e03b length: 12
mcvsftsn.exe

key pos: 0x61ca3f str pos: 0x61cde7 length: 12
avconsol.exe

key pos: 0x61e05f str pos: 0x61ee93 length: 12
avsynmgr.exe

key pos: 0x61db13 str pos: 0x61e3cb length: 12
vstskmgr.exe

key pos: 0x61e113 str pos: 0x61de97 length: 12
webscanx.exe

key pos: 0x619b91 str pos: 0x6195df length: 9
mfewc.exe

key pos: 0x61a5c6 str pos: 0x61ac24 length: 10
mfewch.exe

key pos: 0x627e86 str pos: 0x62801e length: 24
giantantispywaremain.exe

key pos: 0x629774 str pos: 0x6296b7 length: 27
giantantispywareupdater.exe

key pos: 0x62304b str pos: 0x622ea2 length: 17
gcasservalert.exe

key pos: 0x621cc9 str pos: 0x6213a5 length: 15
gcascleaner.exe

key pos: 0x626149 str pos: 0x625efd length: 21
gcasinstallhelper.exe

key pos: 0x620007 str pos: 0x6202fb length: 14
gcasnotice.exe

key pos: 0x6207f5 str pos: 0x6206b3 length: 14
gcasdtserv.exe

key pos: 0x61e1c7 str pos: 0x61dd9b length: 12
gcasserv.exe

key pos: 0x622985 str pos: 0x622b83 length: 17
gcasswupdater.exe

key pos: 0x6197aa str pos: 0x61988b length: 9
fcsms.exe

key pos: 0x619e3c str pos: 0x61a102 length: 10
fcssas.exe

key pos: 0x61a5ee str pos: 0x61ac06 length: 10
nissrv.exe

key pos: 0x6194f5 str pos: 0x619b37 length: 9
dpmra.exe

key pos: 0x61b487 str pos: 0x61b004 length: 11
msseces.exe

key pos: 0x61b7c0 str pos: 0x61c7a6 length: 11
wscntfy.exe

key pos: 0x624d6b str pos: 0x6246d0 length: 19
securitymanager.exe

key pos: 0x625e6a str pos: 0x6260e0 length: 21
aesecurityservice.exe

key pos: 0x621e70 str pos: 0x6220f0 length: 16
deteqt.agent.exe

key pos: 0x61f9fa str pos: 0x61f638 length: 13
omniagent.exe

key pos: 0x61c02c str pos: 0x61bcfe length: 11
nerosvc.exe

key pos: 0x623a0e str pos: 0x623ab0 length: 18
seanalyzertool.exe

key pos: 0x6222e0 str pos: 0x622610 length: 16
spyemergency.exe

key pos: 0x6247da str pos: 0x6245d9 length: 19
spyemergencysrv.exe

key pos: 0x61e3a7 str pos: 0x61de5b length: 12
nlclient.exe

key pos: 0x618e38 str pos: 0x618ec0 length: 8
crdm.exe

key pos: 0x61b6b8 str pos: 0x61c533 length: 11
nmagent.exe

key pos: 0x61d27f str pos: 0x61cea7 length: 12
ehttpsrv.exe

key pos: 0x619441 str pos: 0x619252 length: 9
nod32.exe

key pos: 0x61d927 str pos: 0x61e4eb length: 12
nod32krn.exe

key pos: 0x61e6d7 str pos: 0x61dbd3 length: 12
nod32kui.exe

key pos: 0x61f3ef str pos: 0x61fd2d length: 13
nod32view.exe

key pos: 0x619900 str pos: 0x6197d7 length: 9
cclaw.exe

key pos: 0x61c65c str pos: 0x61b6a2 length: 11
elogsvc.exe

key pos: 0x61867a str pos: 0x6187ca length: 7
nip.exe

key pos: 0x61a3dc str pos: 0x61af12 length: 10
nipsvc.exe

key pos: 0x61c717 str pos: 0x61b962 length: 11
njeeves.exe

key pos: 0x61c898 str pos: 0x61b865 length: 11
npfmsg2.exe

key pos: 0x61a850 str pos: 0x61aa12 length: 10
npfmsg.exe

key pos: 0x61df57 str pos: 0x61e30b length: 12
npfsvice.exe

key pos: 0x61e56f str pos: 0x61d8c7 length: 12
nrmenctb.exe

key pos: 0x61a0da str pos: 0x619da6 length: 10
nvcoas.exe

key pos: 0x61e26f str pos: 0x61e00b length: 12
nvcsched.exe

key pos: 0x619a20 str pos: 0x61968a length: 9
nymse.exe

key pos: 0x61969c str pos: 0x619999 length: 9
zanda.exe

key pos: 0x6187df str pos: 0x618681 length: 7
zlh.exe

key pos: 0x61d2d3 str pos: 0x61cc8b length: 12
ixaptsvc.exe

key pos: 0x61bcf3 str pos: 0x61c000 length: 11
ixavsvc.exe

key pos: 0x61b143 str pos: 0x61b3d7 length: 11
ixfwsvc.exe

key pos: 0x61d7ef str pos: 0x61e503 length: 12
emlproui.exe

key pos: 0x61e65f str pos: 0x61dad7 length: 12
emlproxy.exe

key pos: 0x61952b str pos: 0x619b52 length: 9
mpsvc.exe

key pos: 0x61de4f str pos: 0x61e3bf length: 12
onlinent.exe

key pos: 0x61bd56 str pos: 0x61b77e length: 11
onlnsvc.exe

key pos: 0x61c1e4 str pos: 0x61bd77 length: 11
scanmsg.exe

key pos: 0x61cca3 str pos: 0x61ce83 length: 12
scanwscs.exe

key pos: 0x61b45b str pos: 0x61b2f0 length: 11
tsansrf.exe

key pos: 0x61c3de str pos: 0x61ba75 length: 11
tsatisy.exe

key pos: 0x61d19b str pos: 0x61c9a3 length: 12
tscutynt.exe

key pos: 0x61abde str pos: 0x61a580 length: 10
tsmpnt.exe

key pos: 0x61ab84 str pos: 0x61a4d6 length: 10
upschd.exe

key pos: 0x61b789 str pos: 0x61c814 length: 11
xfilter.exe

key pos: 0x618952 str pos: 0x61874c length: 7
aps.exe

key pos: 0x6187ed str pos: 0x6186e3 length: 7
aus.exe

key pos: 0x61be5e str pos: 0x61c1c3 length: 11
outpost.exe

key pos: 0x620e32 str pos: 0x620f9a length: 15
adminserver.exe

key pos: 0x61a080 str pos: 0x619e14 length: 10
avtask.exe

key pos: 0x61e6fb str pos: 0x61db1f length: 12
clshield.exe

key pos: 0x61b9c5 str pos: 0x61c268 length: 11
console.exe

key pos: 0x61bc0c str pos: 0x61bfd4 length: 11
cpntsrv.exe

key pos: 0x61c840 str pos: 0x61b6e4 length: 11
padfsvr.exe

key pos: 0x6224c0 str pos: 0x622460 length: 16
pasystemtray.exe

key pos: 0x61da83 str pos: 0x61e473 length: 12
pavfnsvr.exe

key pos: 0x61ab70 str pos: 0x61a490 length: 10
pavkre.exe

key pos: 0x61c210 str pos: 0x61bd82 length: 11
pavprot.exe

key pos: 0x61f582 str pos: 0x61fa89 length: 13
pavreport.exe

key pos: 0x61a166 str pos: 0x619d92 length: 10
pnmsrv.exe

key pos: 0x61b0ca str pos: 0x61b58f length: 11
psimsvc.exe

key pos: 0x61ae90 str pos: 0x61a38c length: 10
pavupg.exe

key pos: 0x61a602 str pos: 0x61afe4 length: 10
remupd.exe

key pos: 0x619c7b str pos: 0x61978f length: 9
iface.exe

key pos: 0x61d567 str pos: 0x61edf7 length: 12
pavfires.exe

key pos: 0x61b731 str pos: 0x61c835 length: 11
pavmail.exe

key pos: 0x61e14f str pos: 0x61df0f length: 12
pavprsrv.exe

key pos: 0x61ee9f str pos: 0x61ddd7 length: 12
pavsched.exe

key pos: 0x61d657 str pos: 0x61ea4f length: 12
pavsrv50.exe

key pos: 0x61df63 str pos: 0x61e173 length: 12
pavsrv51.exe

key pos: 0x61eec3 str pos: 0x61db7f length: 12
pavsrv52.exe

key pos: 0x61bf19 str pos: 0x61c06e length: 11
prevsrv.exe

key pos: 0x619924 str pos: 0x619786 length: 9
tpsrv.exe

key pos: 0x61ab8e str pos: 0x61a4ae length: 10
pagent.exe

key pos: 0x61e353 str pos: 0x61dd77 length: 12
pagentwd.exe

key pos: 0x61b90a str pos: 0x61c6b4 length: 11
psctris.exe

key pos: 0x61eccb str pos: 0x61d61b length: 12
apvxdwin.exe

key pos: 0x61a184 str pos: 0x619f5e length: 10
inicio.exe

key pos: 0x61ebc3 str pos: 0x61d747 length: 12
pavbckpt.exe

key pos: 0x61b85a str pos: 0x61b75d length: 11
pavjobs.exe

key pos: 0x61c34f str pos: 0x61b9af length: 11
psctrls.exe

key pos: 0x61a9f4 str pos: 0x61a6b6 length: 10
pshost.exe

key pos: 0x61cd6f str pos: 0x61cfdf length: 12
psimreal.exe

key pos: 0x61da23 str pos: 0x61e863 length: 12
pskmssvc.exe

key pos: 0x61b8bd str pos: 0x61c5c2 length: 11
srvload.exe

key pos: 0x61e0b3 str pos: 0x61ded3 length: 12
webproxy.exe

key pos: 0x61d177 str pos: 0x61cc97 length: 12
avltmain.exe

key pos: 0x620e9b str pos: 0x6210a8 length: 15
firewallgui.exe

key pos: 0x61b403 str pos: 0x61b240 length: 11
pviewer.exe

key pos: 0x619237 str pos: 0x6192be length: 9
pview.exe

key pos: 0x6190b0 str pos: 0x618cd8 length: 8
pmon.exe

key pos: 0x61f693 str pos: 0x61f874 length: 13
qoeloader.exe

key pos: 0x6186ce str pos: 0x6187f4 length: 7
fws.exe

key pos: 0x61c7f3 str pos: 0x61b8ff length: 11
ccenter.exe

key pos: 0x619603 str pos: 0x6199d8 length: 9
ravxp.exe

key pos: 0x61d213 str pos: 0x61cb53 length: 12
rfwproxy.exe

key pos: 0x61b886 str pos: 0x61c575 length: 11
rfwstub.exe

key pos: 0x61d303 str pos: 0x61e98f length: 12
knownsvr.exe

key pos: 0x618482 str pos: 0x6183ef length: 7
ras.exe

key pos: 0x61a0d0 str pos: 0x619f72 length: 10
rasupd.exe

key pos: 0x61a670 str pos: 0x61ab0c length: 10
upfile.exe

key pos: 0x61a648 str pos: 0x61aac6 length: 10
rstray.exe

key pos: 0x61ec9b str pos: 0x61d52b length: 12
ravalert.exe

key pos: 0x618792 str pos: 0x618714 length: 7
rav.exe

key pos: 0x61b73c str pos: 0x61b71b length: 11
ravmond.exe

key pos: 0x61a1f2 str pos: 0x619e50 length: 10
ravmon.exe

key pos: 0x620bf3 str pos: 0x620483 length: 14
ravservice.exe

key pos: 0x61bf50 str pos: 0x61c079 length: 11
ravstub.exe

key pos: 0x61c948 str pos: 0x61bd09 length: 11
ravtask.exe

key pos: 0x61b1c7 str pos: 0x61b348 length: 11
ravtray.exe

key pos: 0x61fc29 str pos: 0x61f37a length: 13
ravupdate.exe

key pos: 0x61e7df str pos: 0x61d987 length: 12
rnreport.exe

key pos: 0x61ccd3 str pos: 0x61ce47 length: 12
rsnetsvr.exe

key pos: 0x61b84f str pos: 0x61c882 length: 11
scanfrm.exe

key pos: 0x61b80d str pos: 0x61c7e8 length: 11
rfwmain.exe

key pos: 0x61ab5c str pos: 0x61a67a length: 10
rfwsrv.exe

key pos: 0x61a8dc str pos: 0x61a83c length: 10
winlog.exe

key pos: 0x622e09 str pos: 0x622fa1 length: 17
omslogmanager.exe

key pos: 0x61b277 str pos: 0x61b42f length: 11
snhwsrv.exe

key pos: 0x621972 str pos: 0x6213ff length: 15
snicheckadm.exe

key pos: 0x62141d str pos: 0x6219ae length: 15
snichecksrv.exe

key pos: 0x61ac92 str pos: 0x619e6e length: 10
snicon.exe

key pos: 0x61992d str pos: 0x61977d length: 9
snsrv.exe

key pos: 0x618dd8 str pos: 0x618ea8 length: 8
smsx.exe

key pos: 0x61d99f str pos: 0x61e7a3 length: 12
svcharge.exe

key pos: 0x61cc7f str pos: 0x61ceb3 length: 12
svdealer.exe

key pos: 0x61bdcf str pos: 0x61bfdf length: 11
svframe.exe

key pos: 0x61a198 str pos: 0x619df6 length: 10
svtray.exe

key pos: 0x619c72 str pos: 0x6197c5 length: 9
sschk.exe

key pos: 0x61b59a str pos: 0x61b63f length: 11
trjscan.exe

key pos: 0x619240 str pos: 0x619306 length: 9
trupd.exe

key pos: 0x6254fc str pos: 0x6253a8 length: 20
ssecuritymanager.exe

key pos: 0x61a9c2 str pos: 0x61a74c length: 10
dltray.exe

key pos: 0x61fa7c str pos: 0x61f604 length: 13
dlservice.exe

key pos: 0x61939f str pos: 0x619213 length: 9
almon.exe

key pos: 0x618d10 str pos: 0x619098 length: 8
lmon.exe

key pos: 0x624483 str pos: 0x6249ee length: 19
savadminservice.exe

key pos: 0x62026f str pos: 0x61fe8d length: 14
savservice.exe

key pos: 0x61e377 str pos: 0x61de13 length: 12
sweepsrv.sys

key pos: 0x61edaf str pos: 0x61d2eb length: 12
swnetsup.exe

key pos: 0x619201 str pos: 0x619396 length: 9
alsvc.exe

key pos: 0x61d87f str pos: 0x61e4bb length: 12
alupdate.exe

key pos: 0x61b9d0 str pos: 0x61c3a7 length: 11
savmain.exe

key pos: 0x61e62f str pos: 0x61dc03 length: 12
sav32cli.exe

key pos: 0x62be09 str pos: 0x62be4b length: 33
certificationmanagerservicent.exe

key pos: 0x626c2a str pos: 0x626694 length: 22
emlibupdateagentnt.exe

key pos: 0x62643d str pos: 0x625e55 length: 21
managementagentnt.exe

key pos: 0x61b7b5 str pos: 0x61c70c length: 11
mgntsvc.exe

key pos: 0x61cb17 str pos: 0x61d273 length: 12
routernt.exe

key pos: 0x61d417 str pos: 0x61ed43 length: 12
schdsrvc.exe

key pos: 0x620635 str pos: 0x620df9 length: 14
scfmanager.exe

key pos: 0x62044b str pos: 0x620ae9 length: 14
scfservice.exe

key pos: 0x61c1fa str pos: 0x61bd40 length: 11
scftray.exe

key pos: 0x61f8cf str pos: 0x61f5a9 length: 13
op_viewer.exe

key pos: 0x619369 str pos: 0x6192a3 length: 9
sgbhp.exe

key pos: 0x61dae3 str pos: 0x61e4a3 length: 12
pctsauxs.exe

key pos: 0x61b676 str pos: 0x61c7dd length: 11
pctsgui.exe

key pos: 0x61c063 str pos: 0x61beed length: 11
pctssvc.exe

key pos: 0x61d783 str pos: 0x61ebf3 length: 12
pctstray.exe

key pos: 0x61c0fd str pos: 0x61bbf6 length: 11
regmech.exe

key pos: 0x61f3bb str pos: 0x61fc84 length: 13
sdtrayapp.exe

key pos: 0x61d837 str pos: 0x61e647 length: 12
svcntaux.exe

key pos: 0x61a5d0 str pos: 0x61aa94 length: 10
swdsvc.exe

key pos: 0x6193d5 str pos: 0x6190ea length: 9
swnxt.exe

key pos: 0x61d4e3 str pos: 0x61e8ab length: 12
execstat.exe

key pos: 0x61b2fb str pos: 0x61b19b length: 11
seestat.exe

key pos: 0x61d57f str pos: 0x61edc7 length: 12
swserver.exe

key pos: 0x619f68 str pos: 0x61a0ee length: 10
slee81.exe

key pos: 0x61b49d str pos: 0x61b0e0 length: 11
kpf4gui.exe

key pos: 0x619d9c str pos: 0x61a076 length: 10
kpf4ss.exe

key pos: 0x620491 str pos: 0x620b75 length: 14
wrspysetup.exe

key pos: 0x61c04d str pos: 0x61bc64 length: 11
acctmgr.exe

key pos: 0x61cceb str pos: 0x61d1fb length: 12
alertsvc.exe

key pos: 0x61faf1 str pos: 0x61f3a1 length: 13
alunotify.exe

key pos: 0x62432d str pos: 0x624081 length: 19
aluschedulersvc.exe

key pos: 0x61eeb7 str pos: 0x61d8d3 length: 12
appsvc32.exe

key pos: 0x618eb0 str pos: 0x618e30 length: 8
ccap.exe

key pos: 0x6194bf str pos: 0x61926d length: 9
ccapp.exe

key pos: 0x61ea37 str pos: 0x61d4d7 length: 12
ccevtmgr.exe

key pos: 0x61c1ad str pos: 0x61bf2f length: 11
ccproxy.exe

key pos: 0x61d243 str pos: 0x61cd1b length: 12
ccpxysvc.exe

key pos: 0x61eb0f str pos: 0x61d3ab length: 12
ccsetmgr.exe

key pos: 0x61bc38 str pos: 0x61bfb3 length: 11
checkup.exe

key pos: 0x6185f5 str pos: 0x6188aa length: 7
cka.exe

key pos: 0x61b1fe str pos: 0x61b634 length: 11
comhost.exe

key pos: 0x61b500 str pos: 0x61b1a6 length: 11
cpdclnt.exe

key pos: 0x61ee6f str pos: 0x61dec7 length: 12
csinject.exe

key pos: 0x61ebe7 str pos: 0x61d327 length: 12
csinsm32.exe

key pos: 0x61d363 str pos: 0x61ead3 length: 12
csinsmnt.exe

key pos: 0x61ab02 str pos: 0x61a56c length: 10
dbserv.exe

key pos: 0x61d573 str pos: 0x61eb1b length: 12
defwatch.exe

key pos: 0x618e78 str pos: 0x618de8 length: 8
defwatch

key pos: 0x61b752 str pos: 0x61b915 length: 11
diskmon.exe

key pos: 0x61e617 str pos: 0x61d9c3 length: 12
djsnetcn.exe

key pos: 0x61ab52 str pos: 0x61a54e length: 10
doscan.exe

key pos: 0x61d9ab str pos: 0x61e5f3 length: 12
dwhwizrd.exe

key pos: 0x619225 str pos: 0x6193f0 length: 9
fwcfg.exe

key pos: 0x61c5cd str pos: 0x61b79f length: 11
ghost_2.exe

key pos: 0x61f3fc str pos: 0x61fc5d length: 13
ghosttray.exe

key pos: 0x61b579 str pos: 0x61b282 length: 11
icepack.exe

key pos: 0x61bf9d str pos: 0x61bcdd length: 11
idsinst.exe

key pos: 0x61d18f str pos: 0x61cd93 length: 12
ispwdsvc.exe

key pos: 0x619963 str pos: 0x619678 length: 9
issvc.exe

key pos: 0x619762 str pos: 0x6198b8 length: 9
isuac.exe

key pos: 0x61995a str pos: 0x619642 length: 9
luall.exe

key pos: 0x624035 str pos: 0x624943 length: 19
lucallbackproxy.exe

key pos: 0x61ddfb str pos: 0x61e0bf length: 12
lucoms~1.exe

key pos: 0x61a5e4 str pos: 0x61ac1a length: 10
lucoms.exe

key pos: 0x619dc4 str pos: 0x61a09e length: 10
mcui32.exe

key pos: 0x61dbeb str pos: 0x61e707 length: 12
navapsvc.exe

key pos: 0x61d933 str pos: 0x61e50f length: 12
navapw32.exe

key pos: 0x61ee57 str pos: 0x61df9f length: 12
navectrl.exe

key pos: 0x61c21b str pos: 0x61baac length: 11
navelog.exe

key pos: 0x61aae4 str pos: 0x61a51c length: 10
navesp.exe

key pos: 0x61e60b str pos: 0x61d7b3 length: 12
navshcom.exe

key pos: 0x61af8a str pos: 0x61a6e8 length: 10
navw32.exe

key pos: 0x619ce8 str pos: 0x61a0f8 length: 10
navwnt.exe

key pos: 0x61b471 str pos: 0x61b64a length: 11
ndetect.exe

key pos: 0x61b0a9 str pos: 0x61b450 length: 11
ngctw32.exe

key pos: 0x61d2df str pos: 0x61eaaf length: 12
ngserver.exe

key pos: 0x61d9cf str pos: 0x61e4df length: 12
nisoptui.exe

key pos: 0x61b0d5 str pos: 0x61b466 length: 11
nisserv.exe

key pos: 0x619990 str pos: 0x619654 length: 9
nisum.exe

key pos: 0x619936 str pos: 0x6197f2 length: 9
nmain.exe

key pos: 0x61da2f str pos: 0x61e833 length: 12
npfmntor.exe

key pos: 0x61d6c3 str pos: 0x61ec3b length: 12
nprotect.exe

key pos: 0x61da5f str pos: 0x61e857 length: 12
npscheck.exe

key pos: 0x61aa80 str pos: 0x61a59e length: 10
npssvc.exe

key pos: 0x61ed37 str pos: 0x61d64b length: 12
nscsrvce.exe

key pos: 0x61af3a str pos: 0x61a3be length: 10
nsctop.exe

key pos: 0x61ac60 str pos: 0x619ee6 length: 10
nsmdtr.exe

key pos: 0x61e54b str pos: 0x61d8f7 length: 12
olfsnt40.exe

key pos: 0x619cf2 str pos: 0x61a10c length: 10
opscan.exe

key pos: 0x61c370 str pos: 0x61b9e6 length: 11
poproxy.exe

key pos: 0x6201ab str pos: 0x61ffeb length: 14
pqibrowser.exe

key pos: 0x61dcdb str pos: 0x61e2f3 length: 12
pqv2isvc.exe

key pos: 0x62052b str pos: 0x620a25 length: 14
pxeservice.exe

key pos: 0x61afbc str pos: 0x61a760 length: 10
qdcsfs.exe

key pos: 0x61c932 str pos: 0x61bcb1 length: 11
qserver.exe

key pos: 0x62143b str pos: 0x6219bd length: 15
reportersvc.exe

key pos: 0x618a88 str pos: 0x618bb0 length: 8
rnav.exe

key pos: 0x61f0bc str pos: 0x61f1b3 length: 13
savfmsesp.exe

key pos: 0x61c88d str pos: 0x61b823 length: 11
savroam.exe

key pos: 0x61bcd2 str pos: 0x61c1b8 length: 11
savscan.exe

key pos: 0x619b01 str pos: 0x6195d6 length: 9
savui.exe

key pos: 0x61a18e str pos: 0x619e00 length: 10
sbserv.exe

key pos: 0x6179f8 str pos: 0x617aa4 length: 4
scan

key pos: 0x61cf4f str pos: 0x61cbb3 length: 12
explicit.exe

key pos: 0x61a85a str pos: 0x61af76 length: 10
semsvc.exe

key pos: 0x61a896 str pos: 0x61a9cc length: 10
sesclu.exe

key pos: 0x61c391 str pos: 0x61b9fc length: 11
sevinst.exe

key pos: 0x61cbfb str pos: 0x61d2c7 length: 12
smsectrl.exe

key pos: 0x61bc01 str pos: 0x61c0e7 length: 11
smselog.exe

key pos: 0x61c82a str pos: 0x61b6ef length: 11
smsesjm.exe

key pos: 0x61ac56 str pos: 0x61a576 length: 10
smsesp.exe

key pos: 0x61c8e5 str pos: 0x61bea0 length: 11
smsesrv.exe

key pos: 0x61e57b str pos: 0x61dbdf length: 12
smsetask.exe

key pos: 0x61abac str pos: 0x61a4ea length: 10
smseui.exe

key pos: 0x61834e str pos: 0x618546 length: 7
sms.exe

key pos: 0x61a35a str pos: 0x61ae22 length: 10
sndmon.exe

key pos: 0x61b9db str pos: 0x61c3b2 length: 11
sndsrvc.exe

key pos: 0x61dfff str pos: 0x61e24b length: 12
spbbcsvc.exe

key pos: 0x61ed13 str pos: 0x61d4b3 length: 12
symlcsvc.exe

key pos: 0x6213d2 str pos: 0x621b34 length: 15
symproxysvc.exe

key pos: 0x61df27 str pos: 0x61e1df length: 12
symsport.exe

key pos: 0x61b6c3 str pos: 0x61b747 length: 11
symtray.exe

key pos: 0x619f9a str pos: 0x619ed2 length: 10
symwsc.exe

key pos: 0x61e743 str pos: 0x61d88b length: 12
sysdoc32.exe

key pos: 0x61f500 str pos: 0x61f9ed length: 13
ucservice.exe

key pos: 0x61e36b str pos: 0x61dd47 length: 12
updtnv28.exe

key pos: 0x61e803 str pos: 0x61d96f length: 12
urllstck.exe

key pos: 0x61dcc3 str pos: 0x61e29f length: 12
usrprmpt.exe

key pos: 0x61ff89 str pos: 0x620093 length: 14
v2iconsole.exe

key pos: 0x619cb1 str pos: 0x619723 length: 9
vpc32.exe

key pos: 0x61b09e str pos: 0x61b5b0 length: 11
vpdn_lu.exe

key pos: 0x61b1dd str pos: 0x61b306 length: 11
vprosvc.exe

key pos: 0x61eecf str pos: 0x61dc0f length: 12
wfxctl32.exe

key pos: 0x61d4a7 str pos: 0x61ec77 length: 12
wfxmod32.exe

key pos: 0x61ed7f str pos: 0x61d37b length: 12
wfxsnt40.exe

key pos: 0x6218dc str pos: 0x621459 length: 15
lucomserver.exe

key pos: 0x6205c5 str pos: 0x620999 length: 14
savfmselog.exe

key pos: 0x6207cb str pos: 0x62075b length: 14
savfmsesjm.exe

key pos: 0x621a35 str pos: 0x621486 length: 15
savfmsectrl.exe

key pos: 0x629882 str pos: 0x6299ab length: 27
savfmsespamstatsmanager.exe

key pos: 0x6203cd str pos: 0x620d7b length: 14
savfmsesrv.exe

key pos: 0x621aad str pos: 0x62132d length: 15
savfmsetask.exe

key pos: 0x61f9d3 str pos: 0x61f4cc length: 13
savfmseui.exe

key pos: 0x618da8 str pos: 0x618f08 length: 8
snac.exe

key pos: 0x618650 str pos: 0x618879 length: 7
ssm.exe

key pos: 0x61f819 str pos: 0x61f770 length: 13
reportsvc.exe

key pos: 0x61a378 str pos: 0x61ae54 length: 10
vptray.exe

key pos: 0x61c037 str pos: 0x61beab length: 11
procexp.exe

key pos: 0x61af26 str pos: 0x61a2ce length: 10
tdimon.exe

key pos: 0x618c58 str pos: 0x618c88 length: 8
tfun.exe

key pos: 0x619759 str pos: 0x619c9f length: 9
tfgui.exe

key pos: 0x61f7cb str pos: 0x61fd6e length: 13
tfservice.exe

key pos: 0x61a15c str pos: 0x619dba length: 10
tftray.exe

key pos: 0x61d5bb str pos: 0x61e9e3 length: 12
tiaspn~1.exe

key pos: 0x61d393 str pos: 0x61ed73 length: 12
traflnsp.exe

key pos: 0x61e203 str pos: 0x61dd8f length: 12
asupport.exe

key pos: 0x61ed5b str pos: 0x61d5d3 length: 12
isntsmtp.exe

key pos: 0x61ba28 str pos: 0x61c25d length: 11
nsmdemf.exe

key pos: 0x61c81f str pos: 0x61b8a7 length: 11
nsmdmon.exe

key pos: 0x61d483 str pos: 0x61eb7b length: 12
nsmdreal.exe

key pos: 0x61b7ec str pos: 0x61c6bf length: 11
nsmdsch.exe

key pos: 0x61a8b4 str pos: 0x61aa08 length: 10
ofcdog.exe

key pos: 0x619573 str pos: 0x619a7a length: 9
pccnt.exe

key pos: 0x61d993 str pos: 0x61e7af length: 12
pccntupd.exe

key pos: 0x61c98b str pos: 0x61d07b length: 12
pcctlcom.exe

key pos: 0x61e2b7 str pos: 0x61dcb7 length: 12
pcscnsrv.exe

key pos: 0x61a36e str pos: 0x61adfa length: 10
schupd.exe

key pos: 0x61b6ce str pos: 0x61c8a3 length: 11
tmntsrv.exe

key pos: 0x6195b2 str pos: 0x619aa7 length: 9
tmpfw.exe

key pos: 0x61c8b9 str pos: 0x61bed7 length: 11
tmproxy.exe

key pos: 0x6190c8 str pos: 0x618e48 length: 8
tmas.exe

key pos: 0x61fff9 str pos: 0x6202df length: 14
entitymain.exe

key pos: 0x61aec2 str pos: 0x61a418 length: 10
aphost.exe

key pos: 0x6208d5 str pos: 0x6206c1 length: 14
lwdmserver.exe

key pos: 0x6185e7 str pos: 0x618895 length: 7
mrf.exe

key pos: 0x620069 str pos: 0x61fec5 length: 14
isntsysmonitor

key pos: 0x61f5f7 str pos: 0x61fa62 length: 13
ofcpfwsvc.exe

key pos: 0x6192c7 str pos: 0x61918c length: 9
dwwin.exe

key pos: 0x6199ab str pos: 0x6196ed length: 9
patch.exe

key pos: 0x61f047 str pos: 0x61f10a length: 13
pccclient.exe

key pos: 0x61dfc3 str pos: 0x61e1eb length: 12
pccguide.exe

key pos: 0x61e1f7 str pos: 0x61dfdb length: 12
pcclient.exe

key pos: 0x61a882 str pos: 0x61af80 length: 10
pccpfw.exe

key pos: 0x61a864 str pos: 0x61a968 length: 10
pcscan.exe

key pos: 0x61e563 str pos: 0x61db67 length: 12
pntiomon.exe

key pos: 0x61e407 str pos: 0x61da53 length: 12
pop3pack.exe

key pos: 0x61ca4b str pos: 0x61d117 length: 12
pop3trap.exe

key pos: 0x624496 str pos: 0x624a99 length: 19
scanmailoutlook.exe

key pos: 0x622afb str pos: 0x622a40 length: 17
smoutlookpack.exe

key pos: 0x61f756 str pos: 0x61f7ff length: 13
webtrapnt.exe

key pos: 0x61fefd str pos: 0x6201e3 length: 14
euqmonitor.exe

key pos: 0x6217a1 str pos: 0x621738 length: 15
smex_activeupda

key pos: 0x62161b str pos: 0x621828 length: 15
smex_master.exe

key pos: 0x620ed7 str pos: 0x620f7c length: 15
smex_remoteconf

key pos: 0x62199f str pos: 0x62140e length: 15
smex_systemwatc

key pos: 0x620715 str pos: 0x620dc1 length: 14
svcgenerichost

key pos: 0x61c8fb str pos: 0x61bf3a length: 11
spntsvc.exe

key pos: 0x6196f6 str pos: 0x619cd5 length: 9
stopp.exe

key pos: 0x620b21 str pos: 0x620413 length: 14
stwatchdog.exe

key pos: 0x61d73b str pos: 0x61eb3f length: 12
usbguard.exe

key pos: 0x6223b0 str pos: 0x6225a0 length: 16
uploadrecord.exe

key pos: 0x61c46d str pos: 0x61ba96 length: 11
sbamsvc.exe

key pos: 0x61be8a str pos: 0x61bfea length: 11
vrvmail.exe

key pos: 0x61a314 str pos: 0x61af08 length: 10
vrvmon.exe

key pos: 0x61aeea str pos: 0x61a2e2 length: 10
vrvnet.exe

key pos: 0x618427 str pos: 0x618466 length: 7
vrv.exe

key pos: 0x6190c0 str pos: 0x618cc0 length: 8
wrsa.exe

key pos: 0x622840 str pos: 0x6222b0 length: 16
networkagent.exe

key pos: 0x6292f3 str pos: 0x6290b7 length: 26
websensecontrolservice.exe

key pos: 0x61d34b str pos: 0x61e8ff length: 12
mpcmdrun.exe

key pos: 0x61c084 str pos: 0x61bc17 length: 11
msascui.exe

key pos: 0x61bf87 str pos: 0x61c0d1 length: 11
msmpeng.exe

key pos: 0x61ce2f str pos: 0x61cbef length: 12
mspmspsv.exe

key pos: 0x61d3e7 str pos: 0x61d633 length: 12
kb891711.exe

key pos: 0x61a616 str pos: 0x61ab48 length: 10
zavaux.exe

key pos: 0x61bdc4 str pos: 0x61c155 length: 11
zavcore.exe

key pos: 0x619ea0 str pos: 0x61a1a2 length: 10
zillya.exe

key pos: 0x61de37 str pos: 0x61ee63 length: 12
zlclient.exe

key pos: 0x619c4e str pos: 0x619519 length: 9
vsmon.exe

key pos: 0x620865 str pos: 0x620731 length: 14
forcefield.exe

key pos: 0x619e28 str pos: 0x619f86 length: 10
iswmgr.exe

key pos: 0x619c57 str pos: 0x6194d1 length: 9
zapro.exe

key pos: 0x61f58f str pos: 0x61fa48 length: 13
zonealarm.exe

key pos: 0x61d333 str pos: 0x61e923 length: 12
mantispm.exe

key pos: 0x61f48b str pos: 0x61f31f length: 13
GDDServer.exe

key pos: 0x618d80 str pos: 0x618f10 length: 8
xagt.exe

key pos: 0x629139 str pos: 0x6292bf length: 26
faild to get process list


key pos: 0x6177e7 str pos: 0x6177f6 length: 3
%v


key pos: 0x628ec9 str pos: 0x628d91 length: 26
cant kill process %v : %v

```
