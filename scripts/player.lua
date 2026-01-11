player = {}

player.x = 10
player.y = 200
player.speed = 200
player.direction = 1 -- 1 for right, -1 for left

player.scale_x = 2
player.scale_y = 2

player.image_idle = love.graphics.newImage('data/images/player/idle.png')
player.image_run = love.graphics.newImage('data/images/player/run.png')

function player.update(dt)
    local dir = 0

    if love.keyboard.isDown('d') then -- use d to move right
        dir = dir + 1
    end

    if love.keyboard.isDown('a') then -- use a to move left
        dir = dir - 1
    end

    if dir ~= 0 then
        player.direction = dir
    end

    player.x = player.x + dir * player.speed * dt
end

function player.draw()
    local img = player.image_idle
    local ox = img:getWidth() / 2
    local oy = img:getHeight() / 2

    love.graphics.draw(img, player.x, player.y, 0, -player.scale_x * player.direction, player.scale_y, ox, oy) -- -player.scale_x to account for the image facing left 
end