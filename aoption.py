# Python code obfuscated by TaNviiR-RiiYaD
 

import base64, codecs
magic = 'aW1wb3J0IG9zCiNDVkFMVUUKYmx1ZT0gJ1wzM1s5NG0nCmxpZ2h0Ymx1ZSA9ICdcMDMzWzk0bScKcmVkID0gJ1wwMzNbOTFtJwp3aGl0ZSA9ICdcMzNbOTdtJwp5ZWxsb3cgPSAnXDMzWzkzbScKZ3JlZW4gPSAnXDAzM1sxOzMybScKY3lhbiAgPSAiXDAzM1s5Nm0iCmVuZCA9ICdcMDMzWzBtJwpwdXJwbGU9IlwwMzNbMDszNW0iCm9zLnN5c3RlbSgnY2xlYXInKQpsaW5lPXllbGxvdysiPT09PT09PT09PT09PT09PT09PT0iK3B1cnBsZSsiPT09PT09PT09PT09PT09PT09PT0iK3JlZCsiPT09PT09PT09PT09PT09PT09PT0iK3B1cnBsZSsiPT09PT09PT09PT09PT09PT09PT0iK3llbGxvdysiPT09PT09PT09PT09PT09PT09PT0iK3llbGxvdysiPT09PT09PT09PT09PT09PT09PT0iK3B1cnBsZSsiPT09PT09PT09PT09PT09PT09PT0iK3JlZCsiPT09PT09PT09PT09PT09PT09PT0iK3B1cnBsZSsiPT09PT09PT09PT09PT09PT09PT0iK3llbGxvdysiPT09PT09PT09PT09P'
love = 'G09CG09CG0vPaAjLJAyCFVtVtcfo2qiCKyyoTkiqlgmqUVbVvVvPvNtVBXIyBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIxBXIyjbtVPQvyMRtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNt4cJEPvNtVBXIxFNtDKI0nT9lVQbtITSBqzyFYHSbGJIRYIWcJJSRVPNtVPNtVPNtVPNtVPNtVPQvyMRXVPNt4cJEVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVBXIxDbtVPQvyMRtVRMuL2Ivo29eVQbtDR1lITSBqzycHvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNt4cJEPvNtVBXIxFNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPQvyMRXVPNt4cJEVPOWoJ8tBvNeBQtjZGLmZwx2AQp4AF'
god = 'AgICAgICAgICAgICAgICAgICAgICAgIOKVkQogICDilZEgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAg4pWRCiAgIOKVmuKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVkOKVnSAKIAogICAgICAgICAgICAgIAoKIiIiKQogI0hFQURFUiAgICAgICAgICAgICAgICAKdGV4dD1saWdodGJsdWUrIlx0XHRDcmVhdGVkIEJ5IDogIit5ZWxsb3crIlRhTnZpaVIgUmlpWWFEIitjeWFuKyJcblxuXHRcdOKYheKYhSAiK3B1cnBsZSsiRG9uJ3QgVHJ5IHRvIEtub3cgTWUiK2N5YW4rIiDimIXimIUgICBcbiIgCm5vdGljZT0iIiAgICAgCmRlZiBoZWFkZXIoKToKCXByaW50KGxvZ28pCglwcmludCh0ZXh0KQoJcHJpbnQobGluZSkKCXByaW50KG5vdGljZSk'
destiny = 'XMTIzVTAioaEuL3DbXGbXPJ9mYaA5p3EyoFtapUy0nT9hZlOwo250LJA0YaO5WlxXMTIzVTSvo3I0XPx6Ptyipl5mrKA0MJ0bW3O5qTuiowZtLJWiqKDhpUxaXDcxMJLtLzSwnltcBtbWo3Zhp3ymqTIgXPqjrKEbo24mVT1unJ4hpUxaXDbXq2ucoTHtIUW1MGbXPJ9mYaA5p3EyoFtaL2kyLKVaXDbWnTIuMTIlXPxXPKOlnJ50XTWfqJHeVxAbo3AyVUyiqKVtG3O0nJ9hVTMlo20tDzIfo3pvX2qlMJIhXlWpoykhJmSqVRAioaEuL3EpoyflKFOOLz91qSkhJmAqVRWuL2gpovNvXDbWo3O0CKA0pvucoaO1qPuwrJShXlWSoaEypvO0nTHtoaIgLzIlVR9zVT9jqTyiovN6VPVcXDbWnJLto3O0CG0vZFV6PtxWL29hqTSwqPtcPtxWLG1coaO1qPtcPtyyoTyzVT9jqQ09VwVvBtbWPJSvo3I0XPxXPDyuCJyhpUI0XPxXPJIfnJLto3O0CG0vZlV6PtxWLzSwnltcPtxWnJ5jqKDbXDbWPDbWMJkmMGbXPDyjpzyhqPtvJJ91VTIhqTIlMJDtLFO3pz9hM28tG3O0nJ9hVvxXPDyuCJyhpUI0XPxX'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
