CREATE USER seek WITH PASSWORD 'seek';
create database seel;

grant all privileges on database seek to seek;


drop table users;
CREATE TABLE users (
    user_id bigserial primary key,
    username varchar(50) not null unique,
    email varchar(100) not null unique,
    password_hash varchar(64) NOT NULL, -- 存储哈希后的密码
    full_name varchar(100),
    contact_number varchar(15),
    created_at timestamp DEFAULT CURRENT_TIMESTAMP, -- 记录创建时间
    updated_at timestamp DEFAULT CURRENT_TIMESTAMP, -- 记录最后更新时间
    CONSTRAINT chk_email_format CHECK (email ~* '^[^@]+@[^@]+\.[^@]+$') -- 简单的电子邮件格式验证
);
COMMENT ON TABLE users IS '用户信息表';

