var config = {
    type: Phaser.AUTO,
    width: 800,
    height: 600,
    physics: {
        default: 'arcade',
        arcade: {
            gravity: { y: 300 },
            debug: false
        }
    },
    scene: [Preloader, GamePlay, Leaderboard,],
    canvas: gameCanvas,
};

var game = new Phaser.Game(config);