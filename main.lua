function love.load()
    require('scripts/player')

    background = love.graphics.newImage('data/images/misc/bg.png')
end

function love.update(dt)
    player.update(dt)
end

function love.draw()
    love.graphics.draw(background, 0, 0, 0, 9, 9) -- example bg image (9, 9) scalex, scaley
    player.draw()
end

