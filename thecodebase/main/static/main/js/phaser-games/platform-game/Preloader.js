

class Preloader extends Phaser.Scene {

    constructor ()
    {
        super('Preloader');
    }

    preload()
    {
        var current_folder = '/static/main/js/phaser-games/platform-game/'

        this.load.image('sky', current_folder + 'assets/sky.png');
        this.load.image('ground', current_folder + 'assets/platform.png');
        this.load.image('star', current_folder + 'assets/star.png');
        this.load.image('bomb', current_folder + 'assets/bomb.png');
        this.load.spritesheet('dude',
            current_folder + 'assets/dude.png',
            { frameWidth: 32, frameHeight: 48 }
        );
        this.load.image('sky', current_folder + 'assets/sky.png');
        this.load.bitmapFont('arcade', current_folder + 'assets/fonts/bitmap/arcade.png', current_folder + 'assets/fonts/bitmap/arcade.xml');
    }

    create()
    {
        this.anims.create({
            key: 'left',
            frames: this.anims.generateFrameNumbers('dude', { start: 0, end: 3 }),
            frameRate: 10,
            repeat: -1
        });

        this.anims.create({
            key: 'turn',
            frames: [ { key: 'dude', frame: 4 } ],
            frameRate: 20
        });

        this.anims.create({
            key: 'right',
            frames: this.anims.generateFrameNumbers('dude', { start: 5, end: 8 }),
            frameRate: 10,
            repeat: -1
        });

        this.scene.start('GamePlay');
    }

}
