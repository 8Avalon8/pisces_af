pisces_af
===
Pisces_af is an UI automated test framework based on Sikulix and was used for Game UI testing. It's easy to use and can easy to use some continuous integration tools like Jenkins to manage several clients to run different autotest script.

**Requirement**  

`Sikulix 1.1.2`  (include java environment) : https://raiman.github.io/SikuliX-2014/nightly.html  
`python2.7` and `pywin32`    (If you want to locate the game window in windows system, you will need it)  

**Environment variables**  

In Windows system, you need add some environment variables
`SIKULIX_HOME`：Your sikulix folder e.g. `D:\SikuliX1.1.2\`
`JAVA_HOME` : Your JDK folder path
`CLASSPATH` : `%SIKULIX_HOME%sikulixapi.jar`

**Path configuration**
`runsikulix.bat`:
```cmd
"%JAVA_HOME%\bin\java.exe" %PARMS% -jar "%SIKULIX_HOME%%SJAR%.jar" -c -d 3 -f -r "E:\pisces_af\"
```
`gl.py`:
```python
project_path = "E:\\pisces_af"
```
`pisces_af.py`:
```python
project_path = "E:\\pisces_af"
```
