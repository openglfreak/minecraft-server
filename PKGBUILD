# Maintainer: Torge Matthies <openglfreak at googlemail dot com>

pkgname=minecraft-server
pkgver=0.1.0
pkgrel=1
pkgdesc="Minecraft server"
arch=('x86_64')
license=('proprietary')
depends=('java-runtime' 'python' 'python-systemd')
optdepends=('socat: minecraft-server-console command')
source=('broadcast-socket.py'
        'console-connect.sh'
        'idle-stop.sh'
        'minecraft-server.conf'
        'minecraft-server-console@.service'
        'minecraft-server-console@.socket'
        'minecraft-server-idle-stop@.service'
        'minecraft-server-idle-stop@.timer'
        'minecraft-server@.service'
        'minecraft-server@.socket'
        'minecraft-server-stdin@.socket'
        'minecraft-server-stdout@.socket'
        'minecraft-server-workaround-7069-before@.service'
        'minecraft-server-workaround-7069-after@.service'
        'player-count.py'
        'server-launch.sh'
        'socket-generator.sh')
sha256sums=('d3ba80c7706d83d25996a0072e426cbfdefe73d3557135c56c38c3124b4bb4db'
            'f1a71ecd7e02dc657ded2948bd73e5067ff93223b24c7733abd00cc3c5c57a9f'
            'edbe8f50077773cd19c45201f61fe89a793496743dd10b81f7107939fa2badeb'
            '0eda1f642b5c3831ac387c5b51586f35ea33719e989f8db0b24f907eab2c5a80'
            '00a2352533b46705d6c382107285015b5fa12078113102fad2a4fe4bc46cacd0'
            '365eb6fd3dec27c3d303c22750869b615a98bfc7b77fa45f2ca656b769cf734f'
            'c6d5987857c9dbf448b1fb3c2a528ff1ed79f682f21f77de3121bc68b6daa014'
            '7759c1d94e499638dcd48d55da82c4741d4f9a2f3bf5933eab3f40301ba735d7'
            '8854bc0fc23ed061502fa9d686120d9711e632785e2ba4c5fe7192e78efd290e'
            '3d90a2aaf181fbd1eb6ee4ae23fadd1a090d370970785dce0447a0a4e605c301'
            'b81bdacdb5e97c3eaf2e5ad95e536200041d54d98029b6f01a6b2b1bc40df863'
            'bb15eaa9678a46a940442c92f8f31019512a7a3ebf003e1c15e5bdbd00706d56'
            '221a9753c683f057ba928dc4e63708f602982b88dc77342313d7aba830862c57'
            '64ce44edb0b7889751089d1daad916d5cad08c7d5a6751ac6bb6f1474c3e4d8d'
            '37e00de087ac89ae79b1c64974ff99dea35fde6f1b14907e31a4a9eee75e2097'
            'd17be777065c7cff9906b00c27e3f734c810f585cbf56206c65db6a116450964'
            'a8a9ddf2a95b814308a2eef32c75cdfae3af895c6e065c126b8625e5edd98cce')

package() {
    install -Dm755 "${srcdir}/broadcast-socket.py" "${pkgdir}/usr/lib/minecraft-server/broadcast-socket.py"
    install -Dm755 "${srcdir}/console-connect.sh" "${pkgdir}/usr/bin/minecraft-server-console"
    install -Dm755 "${srcdir}/idle-stop.sh" "${pkgdir}/usr/lib/minecraft-server/idle-stop.sh"
    install -Dm644 "${srcdir}/minecraft-server.conf" "${pkgdir}/usr/lib/sysusers.d/minecraft-server.conf"
    install -Dm644 "${srcdir}/minecraft-server-console@.service" "${pkgdir}/usr/lib/systemd/system/minecraft-server-console@.service"
    install -Dm644 "${srcdir}/minecraft-server-console@.socket" "${pkgdir}/usr/lib/systemd/system/minecraft-server-console@.socket"
    install -Dm644 "${srcdir}/minecraft-server-idle-stop@.service" "${pkgdir}/usr/lib/systemd/system/minecraft-server-idle-stop@.service"
    install -Dm644 "${srcdir}/minecraft-server-idle-stop@.timer" "${pkgdir}/usr/lib/systemd/system/minecraft-server-idle-stop@.timer"
    install -Dm644 "${srcdir}/minecraft-server@.service" "${pkgdir}/usr/lib/systemd/system/minecraft-server@.service"
    install -Dm644 "${srcdir}/minecraft-server@.socket" "${pkgdir}/usr/lib/systemd/system/minecraft-server@.socket"
    install -Dm644 "${srcdir}/minecraft-server-stdin@.socket" "${pkgdir}/usr/lib/systemd/system/minecraft-server-stdin@.socket"
    install -Dm644 "${srcdir}/minecraft-server-stdout@.socket" "${pkgdir}/usr/lib/systemd/system/minecraft-server-stdout@.socket"
    install -Dm644 "${srcdir}/minecraft-server-workaround-7069-before@.service" "${pkgdir}/usr/lib/systemd/system/minecraft-server-workaround-7069-before@.service"
    install -Dm644 "${srcdir}/minecraft-server-workaround-7069-after@.service" "${pkgdir}/usr/lib/systemd/system/minecraft-server-workaround-7069-after@.service"
    install -Dm755 "${srcdir}/player-count.py" "${pkgdir}/usr/lib/minecraft-server/player-count.py"
    install -Dm755 "${srcdir}/server-launch.sh" "${pkgdir}/usr/lib/minecraft-server/server-launch.sh"
    install -Dm755 "${srcdir}/socket-generator.sh" "${pkgdir}/usr/lib/systemd/system-generators/minecraft-server-socket-generator.sh"
}
