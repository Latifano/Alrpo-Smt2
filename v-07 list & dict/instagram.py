class Instagram:
    def __init__(self, profil, follower, following):
        self.profil = profil
        self.follower = follower
        self.following = following

    def Showinfo(self):
        print(
            f'\nNama IG : {self.profil}\nFollower : {self.follower}\nFollowing : {self.following}\n')

    def Post(self, posting, caption):
        self.post = posting
        self.capt = caption
        print(f'Foto, Video atau IGTV telah dibuat : {self.post}')
        print(f'Dengan Caption : {self.capt}\n')

    def StoryBoomerang(self):
        print('Boomerang Telah Berhasil Dibuat !\n')

    def StoryFoto(self):
        print('Foto Telah Berhasil Dibuat !\n')

    def LiveIG(self):
        print('Live IG sedang berlangsung !\n')

    # def follow(self):


romi = Instagram('@ikromi_ltfn', 467, 243)  # Object dan Atribut
yosehpine = Instagram('@yosephine', 500, 100)

romi.Showinfo()
romi.Post('fotoLebaran.jpg', 'Foto Lebaran bareng keluarga')
romi.Post('videotutorial.mp4',
          'Halo guys kali ini saya akan membagikan tutorial menulis source code dengan rapi dan efisien')
romi.StoryBoomerang()
romi.StoryFoto()
romi.LiveIG()
