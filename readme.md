## bpatch
This tool is used to patch a payload into the `jab3b4ded00cb34b3cc77a6699f87ac10753fa701.b` file, which is created by [jjpatcher](https://github.com/farid1991/jjpatcher) [a2 runtime patcher](https://mobilefree.justdanpo.ru/newbb_plus/viewtopic.php?topic_id=3591).


### Prerequisites
- **Python 3.x**
- *Optional*: [**FASMARM**](https://github.com/farid1991/jjpatcher/tree/main/fasmarm) (for assembling *bpatchgo.asm*)


### How to obtain the jabxxx file
1. Upload `customize_upgrade.xml` in the script directory into `/tpa/preset/custom` using SEFP2 or SETool.
2. The jabxxx file will be saved in `/usb/other/jab3b4ded00cb34b3cc77a6699f87ac10753fa701.b`
3. Copy jabxxx file to PC via `Bluetooth`, `MTP`, or `Mass Storage`


### Patching
Run the following command:
```
python bpatch.py jab3b4ded00cb34b3cc77a6699f87ac10753fa701.b
```


### After patching
Upload back patched jabxxx to: 
```
/tpa/preset/system/ams/jab3b4ded00cb34b3cc77a6699f87ac10753fa701.b
``` 
using **A2Uploader**(*DB3150 and DB32XX with max CID53*), **SEFP2** or **SETool**. 


### More information
- For additional details, visit:  
[MobileFree Forum - a2 runtime patcher](https://mobilefree.justdanpo.ru/newbb_plus/viewtopic.php?topic_id=3591)
- Auto builder [jjpatcher](https://github.com/farid1991/jjpatcher)