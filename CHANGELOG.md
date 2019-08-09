# Changelog
All notable changes to this project will be documented in this file.

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2019.08.08
### Added
- Introduced new ip_network method within span_ip() function to omit strict IP networks and allow subnetting of networks with host bits set (e.g. 192.168.1.10/24).

### Changed
- Commented out deprecated conditional statement within span_ip() function.
