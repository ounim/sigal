# -*- coding:utf-8 -*-

from __future__ import division

import os

from sigal.video import video_size, generate_video
from sigal.settings import create_settings

CURRENT_DIR = os.path.dirname(__file__)
TEST_VIDEO = 'stallman software-freedom-day-low.ogv'
SRCFILE = os.path.join(CURRENT_DIR, 'sample', 'pictures', 'video', TEST_VIDEO)


def test_video_size():
    size_src = video_size(SRCFILE)
    assert size_src == (480, 270)


def test_generate_video_fit_height(tmpdir):
    """largest fitting dimension is height"""

    base, ext = os.path.splitext(TEST_VIDEO)
    dstfile = str(tmpdir.join(base + '.webm'))
    settings = create_settings(video_size=(50, 100))
    generate_video(SRCFILE, dstfile, settings)

    size_src = video_size(SRCFILE)
    size_dst = video_size(dstfile)

    assert size_dst[0] == 50
    # less than 2% error on ratio
    assert abs(size_dst[0]/size_dst[1] - size_src[0]/size_src[1]) < 2e-2


def test_generate_video_fit_width(tmpdir):
    """largest fitting dimension is width"""

    base, ext = os.path.splitext(TEST_VIDEO)
    dstfile = str(tmpdir.join(base + '.webm'))
    settings = create_settings(video_size=(100, 50))
    generate_video(SRCFILE, dstfile, settings)

    size_src = video_size(SRCFILE)
    size_dst = video_size(dstfile)

    assert size_dst[1] == 50
    # less than 2% error on ratio
    assert abs(size_dst[0]/size_dst[1] - size_src[0]/size_src[1]) < 2e-2


def test_generate_video_dont_enlarge(tmpdir):
    """video dimensions should not be enlarged"""

    base, ext = os.path.splitext(TEST_VIDEO)
    dstfile = str(tmpdir.join(base + '.webm'))
    settings = create_settings(video_size=(1000, 1000))
    generate_video(SRCFILE, dstfile, settings)

    size_src = video_size(SRCFILE)
    size_dst = video_size(dstfile)

    assert size_src == size_dst
