$(function() {"use strict";

	var stickOnScroll;

	//Header Option
	$('#header').addClass('normal');
	//Choose Here Class Name (normal or fixed or intelligent);

	var video1;
	var left_off;
	var top_off;
	var myPara = document.createElement("body");
	// datepicker
	if ($('.pick-date').length) {
		/*$('.pick-date').datepicker({
			format : "yyyy/mm/dd"
		});*/
	$(".pick-date").persianDatepicker({theme: 'lightorang',	formatDate : "YYYY/0M/0D"});       
	}
	
	$('.drop-down-parent').on('click', function() {
		if ($(window).width() <= 767) {
			$(this).find('.drop-down').slideToggle();
			$(this).siblings().find('.drop-down').slideUp();
			$(this).toggleClass('active-arrow');
			$(this).siblings().removeClass('active-arrow');
		}
	});
	if ($('.time-pick').length) {
		$('.time-pick').timepicker({
			'scrollDefault' : 'now'
		});
	}

	if ($("#blog-slider").length) {
		$("#blog-slider").owlCarousel({
			autoplay : false,
			rtl:true,
			/*itemsDesktop : [1199, 3],
			itemsDesktopSmall : [979, 3],
			itemsTablet : [768, 3],
			itemsMobile : [767, 1],*/
			responsive:{
				0:{
				items:1,
				},
				1000:{
				items:3,
				},
				768 :{
				items:3,
				}
			},
			nav : true,
			navText : ["بعدی ","قبلی"],
			pagination : false

		});
	}

	if ($("#blog-page-post").length) {
		$("#blog-page-post").owlCarousel({
			autoplay : false,
			rtl:true,
			/*items : 2,
			itemsDesktop : [1199, 2],
			itemsDesktopSmall : [979, 2],
			itemsTablet : [768, 2],
			itemsMobile : [767, 1],*/
			responsive:{
				0:{
				items:1,
				},
				1000:{
				items:2,
				},
				768 :{
				items:2,
				}
			},
			nav : true,
			navText : ["بعدی ","قبلی"],
			pagination : false

		});
	}

	if ($(".review-profile").length) {
		$(".review-profile").owlCarousel({
			autoplay : false,
			rtl:true,
			items : 1,
			itemsDesktop : [1199, 1],
			itemsDesktopSmall : [979, 1],
			itemsTablet : [768, 1],
			itemsMobile : [767, 1],
			nav : true,
			navText : ["بعدی ","قبلی"],
			pagination : false

		});
	}
	if ($(".car-parts-slider").length) {
		var $owl_car_parts = $(".car-parts-slider").owlCarousel({
			autoplay : true,
			autoplayTimeout:2000,
			autoplayHoverPause:true,
			rtl:true,
			items : 1,
			nav : false,
			pagination : true,
			loop:true,
		});

		setInterval(function() {
			$('.vehicles-carousal-thumb').find('li').removeClass('active');
			var page_index = $('.owl-dots .owl-dot.active').index();
			$('.vehicles-carousal-thumb').find('li').eq(page_index).addClass('active');
		}, 100);

		$('.vehicles-carousal-thumb li').on('click', function() {
			$(this).siblings("li").removeClass('active');
			$(this).addClass('active');
			var index = $(this).index();
			$owl_car_parts.trigger('to.owl.carousel', index)
		});
	}

	if ($(".safety-slider").length) {
		$(".safety-slider").owlCarousel({
			autoplay:true,
			autoplayTimeout:2000,
			autoplayHoverPause:true,
			rtl:true,
			items : 1,
			nav : true,
			navText : ["بعدی ","قبلی"],
			pagination : false
		});
	}

	// Range slider js start here

	if ($("#slider").length) {
		$("#slider").slider({
			rtl:true,
			range : true,
			min : 24,
			max : 700,
			values : [24, 320],
			slide : function(event, ui) {
				$("#amount1").val(ui.values[0] + " ریال");
				$("#amount2").val(ui.values[1] + " ریال");
			}
		});
		$("#amount1").val($("#slider").slider("values", 0) + " ریال");
		$("#amount2").val($("#slider").slider("values", 1) + " ریال");
	}

	if ($('.select').length) {
		$('.select').selectBox();
	}

	$('.fa-search').on('click', function() {
		$('.search-bar').slideToggle();
	});

	$('.play-btn').on('click', function() {
		video1 = '<iframe src="' + $('.video img').attr('data-video') + '"></iframe>';

		jQuery('.video img').after(video1);
		return false;

	});

	$('.audio-wrap').on('click', function() {

	});

	if ($('.fancybox-button').length) {
		$(".fancybox-button").fancybox();
	}
	
//================= Header Style function ================
	if ($('#header').hasClass('fixed')) {
		$('#header').next().addClass('top-m');
	}
	if ($('#header').hasClass('intelligent')) {
		$('#header').next().addClass('top-m');
	};

	var class_pr = $('body').attr('class');
	var headerHeight = $('#header').outerHeight();
	var st = $(window).scrollTop();
	stickOnScroll = function() {

		if ($('#header').hasClass("intelligent")) {

			$('#header').removeClass('normal');
			$('#header').next().addClass('top-m');
			var pos = $(window).scrollTop();

			if (pos > headerHeight) {
				if (pos > st) {
					$('#header').addClass('simple')
					$('#header.simple').removeClass('down');
					$('#header.simple').addClass('fixed up');

				} else {
					$('#header.simple').removeClass('up');
					$('#header.simple').addClass('fixed down');

				}
				st = pos;

			} else {
				$('#header.simple').removeClass('fixed down up simple');
			}
			if (pos == $(document).height() - $(window).height()) {
				$('#header.simple').removeClass('up');
				$('#header.simple').addClass('fixed down');
			}

		} else if ($('body').hasClass("fix")) {

			$('#header').next().addClass('top-m');
			$('#header').addClass('simple fixed');
			$('#header').removeClass('down up');
			$('#wrapper').css({
				paddingTop : 0
			});
		} else {

			$('#header.simple').removeClass('fixed down up simple');
			$('#header').addClass('normal');

			$('#wrapper').css({
				paddingTop : 0
			});
		}
	};
	stickOnScroll();
	$(window).scroll(function() {
		stickOnScroll();
	});
		
$(window).load(function() {
		$("#loading").fadeOut(500);
		if ($('.flexslider').lenght) {
			$('.flexslider').flexslider({
				animation : "slide",
				customDirectionNav : $(".custom-navigation a"),
				controlNav : false
			});

		}
		$(".loader").fadeOut(500);
	});
	// end for sticky header
});