create table if not exists `film_tv_list`(
    `id` int not null auto_increment comment '行号',
    `title` varchar(100) default '' comment '影视标题',
    `abstract` varchar(255) default '' comment '描述',
    `image_url` varchar(100) default '' comment '图片 URL',

    `create_date` datetime not null comment '影视创建时间',
    `update_date` datetime not null comment  '影视更新时间',

    `tags` varchar(100) default '' comment '提示标签',

    `source_domain` varchar (20) not null comment '网站源 地址',

    `detail_url` varchar(100) not null comment '详情地址',

    `click_amount` int not null default 0 comment '点击量',
    `likes_amount` int not null default 0 comment '点赞数',
    `comment_amount` int not null default 0 comment '评论数',

    `category` varchar(20) default '' comment '类型',

    primary key (`id`)
)ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='影视 列表';