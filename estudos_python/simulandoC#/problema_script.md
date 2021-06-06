eu instalei o dotnet e tudo mais, mas eu tenho o Run Code quando eu dou Ctrl+Alt+N ele não roda me retorna a seguinte mensagem.

```
Comando 'scriptcs' não encontrado, você quis dizer:

  comando 'scripts' do deb gitlab-runner (11.2.0+dfsg-2ubuntu1)

Experimente: sudo apt install <deb name>

```
Já fiz o que pede, na mensagem e não resolveu, talvez o problema esteja no arquivo launch.json o problema, sabem como configurar para que rode o comando: 

Quando dou esse comando ele funciona certo no terminal.
```
dotnet run
```

```
Hello World!
```

Meu código:
arquivo Program.cs

```

using System;

namespace con
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Ola mundo!");
        }
    }
}
```

Meu arquivo launch.json:
```
"version": "0.2.0",
    "configurations": [
        {
            // Use IntelliSense to find out which attributes exist for C# debugging
            // Use hover for the description of the existing attributes
            // For further information visit https://github.com/OmniSharp/omnisharp-vscode/blob/master/debugger-launchjson.md
            "name": ".NET Core Launch (console)",
            "type": "coreclr",
            "request": "launch",
            "preLaunchTask": "build",
            // If you have changed target frameworks, make sure to update the program path.
            "program": "${workspaceFolder}/bin/Debug/net5.0/con.dll",
            "args": [],
            "cwd": "${workspaceFolder}",
            // For more information about the 'console' field, see https://aka.ms/VSCode-CS-LaunchJson-Console
            "console": "internalConsole",
            "stopAtEntry": false
        },
        {
            "name": ".NET Core Attach",
            "type": "coreclr",
            "request": "attach",
            "processId": "${command:pickProcess}"
        }
    ]
}

```

Eu instalei o svm para poder instalar esse programa scriptcs, mas também não deu certo

```
svm install 0.4.2

 scriptcs version manager - 0.4.2 

/home/roberto/.svm/bin/svm: linha 41: [: !=: esperava operador unário
 Downloading version '0.4.2' from ''. 
/home/roberto/.svm/bin/svm: linha 134: [: !=: esperava operador unário
 Installing version '0.4.2'. 
mv: não foi possível obter estado de '/home/roberto/.svm/temp/eeb7b42a-3738-4391-ac1d-3daeadb769f6/ScriptCs.0.4.2.nupkg': Arquivo ou diretório inexistente
ls: não foi possível acessar '/home/roberto/.svm/versions/0.4.2': Arquivo ou diretório inexistente
 Version '0.4.2' is now available. 
 Consider using svm use <version> to set it as the active scriptcs version.
```

Pensei que era algum problema da versão então rodei esse código

```
svm install -l

 scriptcs version manager - 0.4.2 

/home/roberto/.svm/bin/svm: linha 41: [: !=: esperava operador unário
 The following scriptcs versions are available for installation:
 
  0.17.1
  0.17.0
  0.16.1
  0.16.0

```

Tentei instalar todas essas versões nenhuma deu certo.
Essa foi a mensagem de erro que me retornava:

```
svm install 0.17.1

scriptcs version manager - 0.4.2 

/home/roberto/.svm/bin/svm: linha 41: [: !=: esperava operador unário
 Downloading version '0.17.1' from 'http://chocolatey.org/api/v2/package/ScriptCs/0.17.1'. 
 The NuGet package could not be downloaded from 'http://chocolatey.org/api/v2/package/ScriptCs/0.17.1'. 

```

Considerei que era porque o nuget não estava instalado então rodei o comando:

```
sudo apt-get install nuget
```

Mesmo assim continuou o problema. 

Então tentando compilar o scriptcs fiz o seginte linha de comando:

```
git clone https://github.com/scriptcs/scriptcs.git
cd scriptcs/
./build.sh
```

Daí me retornava um erro:
Ao ligado ao mono, então executei o seguinte código:

```
sudo apt install gnupg ca-certificates
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
echo "deb https://download.mono-project.com/repo/ubuntu stable-focal main" | sudo tee /etc/apt/sources.list.d/mono-official-stable.list
sudo apt update
sudo apt upgrade
```
Eu escolhi aquele comando era o que falava [aqui](https://www.mono-project.com/download/stable/) para sistema ubuntu 20.04.

Então resolvi tentar o do ubuntu 18.04, com o seguinte código:

```
sudo apt install gnupg ca-certificates
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
echo "deb https://download.mono-project.com/repo/ubuntu stable-bionic main" | sudo tee /etc/apt/sources.list.d/mono-official-stable.list
sudo apt update
```
E atualizei e dei upgrade:

```
sudo apt update
sudo apt upgrade
```

E tentei compilar novamente:

```
./build.sh
```

E saida foi muita coisa, alguns texto amarelos, mas no final foi isso que me retorno:

```
Finished Target: Pack

---------------------------------------------------------------------
Build Time Report
---------------------------------------------------------------------
Target     Duration
------     --------
Clean      00:00:00.1001352
Build      00:00:18.3125670
Test       00:01:18.7285421
Pack       00:00:07.4113952
Total:     00:01:44.6120209
---------------------------------------------------------------------
Status:    Ok
---------------------------------------------------------------------

```

Fui no meu Vscode e tentei fazer o comando Ctrl+Alt+N no terminal foi isso que me foi retornado:

```
scriptcs "/home/roberto/Documentos/dot/con/Program.cs"
 The active scriptcs could not be found at '/home/roberto/.svm/versions/__NO_ACTIVE_VERSION__/scriptcs.exe'. Use 'svm use <version>' to correctly set the active scriptcs version.
```

Aparentemente é a versão que não foi ativada, então tentei:

```
svm install 0.4.2
```

Veio a seguinte mensagem de erro:

```

 scriptcs version manager - 0.4.2 

/home/roberto/.svm/bin/svm: linha 41: [: !=: esperava operador unário
 Downloading version '0.4.2' from ''. 
/home/roberto/.svm/bin/svm: linha 134: [: !=: esperava operador unário
 Installing version '0.4.2'. 
mv: não foi possível obter estado de '/home/roberto/.svm/temp/17364924-e674-4e16-abe8-e6cf316645dc/ScriptCs.0.4.2.nupkg': Arquivo ou diretório inexistente
ls: não foi possível acessar '/home/roberto/.svm/versions/0.4.2': Arquivo ou diretório inexistente
 Version '0.4.2' is now available. 
 Consider using svm use <version> to set it as the active scriptcs version.
```

Então rodei os comandos:

```
svm install -l
svm install 0.17.1
cd .svm/versions/
wget http://chocolatey.org/api/v2/package/ScriptCs/0.17.1
mv '0.17.1' 'ScriptCs.0.17.1.nupkg'
cd ../
nano version
``` 

Apaguei tudo que tava no documento de texto e escrevi. 
```
0.17.1
```
E salvei, executei esses comandos:

```
cd
svm install 0.17.1 -from '.svm/versions/ScriptCs.0.17.1.nupkg'
svm use 0.17.1
scriptcs -Version
```

E scriptcs, acredito eu, está funcionado, mas quando no vscode e e faço o atalho Ctrl+Alt+N ele me retorna.

```
Unexpected named argument: home/roberto/Documentos/dot/con/Program.cs
```
Mas quando executo esse comando:

```
scriptcs -Version
```

O terminal me retorna:

```
               _       _
 ___  ___ _ __(_)_ __ | |__ ___ ___
/ __|/ __| '__| | '_ \| __// __/ __|
\__ \ (__| |  | | |_) | |_| (__\__ \
|___/\___|_|  |_| .__/ \__\\___|___/
                |_| Version: 0.17.1
```

Então agora tenho que configura o Vscode né? Porque parece que programa esta funcionando. Como faço para configurar o Vscode?


## O que me resolveu foi criar um arquivo `settings.json`, e colocar código dentro dele:


```
{
    "code-runner.executorMap": { "csharp": "dotnet run" }
}

```
