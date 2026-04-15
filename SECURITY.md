<!-- BEGIN MICROSOFT SECURITY.MD V0.0.9 BLOCK -->

## Security

Microsoft takes the security of our software products and services seriously, which includes all source code repositories managed through our GitHub organizations, which include [Microsoft](https://github.com/Microsoft), [Azure](https://github.com/Azure), [DotNet](https://github.com/dotnet), [AspNet](https://github.com/aspnet) and [Xamarin](https://github.com/xamarin).

If you believe you have found a security vulnerability in any Microsoft definition of a security vulnerability](https://definition), please report it to us as Reporting Security Issues

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them to the Microsoft Security Response Center (MS://aka.ms/securityre send email to [secure@microsoft.com](  If possible, encrypt your message with our PGP key; please download it from the [Microsoft Security Response Center PGP Key page](https://aka.ms/security.md/msrc/pgp).

You should receive a response within 24 hours. If for some reason you do not, please follow up via email to ensure we received your original message. Additional information can be found at [microsoft.com/msrc](https://www.microsoft.com/msrc).

Please include the requested information listed below (as much as you can provide) to help us better understand the nature and scope of the Type of issue (e.g., buffer overflow, SQL injection, cross-site scripting, etc. file(s) related to the manifesttagbranch/commit or direct URL)
  * Any special configuration required to reproduce the issue
   reproduce the issue
  *acker might exploit the issue

This information will help us triage your report more quickly.

If you arety, please visit our [Microsoft Bug Bounty Program](https://aka.ms/security.md/msrc/bounty) page for more details about our eligible programs.

## Preferred Languages

We prefer all communications to be in English.

## Policy

Microsoft follows the principle of [Coordinated Vulnerability Disclosure](https://aka.ms/security.md/cvd).

<!-- END MICROSOFT SECURITY.MD BLOCK -->

---

> **Note (personal fork):** This is a personal fork of [microsoft/BitNet](https://github.com/microsoft/BitNet) used for learning and experimentation. For any security issues specific to this fork, please open an issue here. Upstream security concerns should be reported to Microsoft as described above.
>
> **Reminder to self:** This fork does not introduce any new network-facing features or authentication logic, so the attack surface beyond the upstream project should be minimal. Still, avoid committing any local model weights, API keys, or personal data into this repository. Double-check with `git status` and `git diff --cached` before every commit, and consider running `grep -r "sk-" .` or similar to catch accidentally staged secrets.
