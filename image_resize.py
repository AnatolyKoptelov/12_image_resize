import os
import sys
import math
import argparse
import PIL.Image
from os.path import dirname


def get_args(extensions):
    parser = argparse.ArgumentParser(
        description='{}{}{}'.format(
            'Resize and/or convert an image. Type it location. ',
            'Supported files extensions: ',
            str(extensions),
        )
    )
    parser.add_argument(
        'fname',
        metavar='fname',
        help='File path'
    )
    parser.add_argument(
        '-W',
        '--width',
        type=int,
        help='Set a new width of image'
    )
    parser.add_argument(
        '-H',
        '--height',
        type=int,
        help='Set a new height of image',
    )
    parser.add_argument(
        '-s',
        '--scale',
        type=float,
        help='{} {}'.format(
            'Set a scaling coefficient of image.',
            'Use s<1 for reduction'
        )
    )
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        help='Set a new filename',
    )
    return parser.parse_args()


def get_file_extension(fname):
    return fname.split('.')[-1].lower()


def check_args(args, extensions, get_file_extension):
    if not os.path.isfile(args.fname):
        return 1, '{} {} {}'.format(
            'Image file',
            args.fname,
            'is not found',
        )
    if get_file_extension(args.fname) not in extensions:
        return 2, '.{} {}'.format(
            get_file_extension(args.fname),
            'files are not supported',
        )
    if args.scale and (args.width or args.height):
        return 3, '{}{}\n{}'.format(
            'Cannot to use both resize methods: ',
            'scaling and resizing by side sizes',
            'Try to use one of them.',
        )
    if args.output:
        extensions.append('pdf',)
        if get_file_extension(args.output) not in extensions:
            return 4, '.{} {}'.format(
            get_file_extension(args.output),
            'files are not supported',
            )
        out_path = dirname(args.output) or dirname(args.fname) or os.getcwd()
        if not os.access(out_path, os.W_OK):
            return 5, '{} {}'.format(
                'Your output path is incorrect or',
                'permissions denied.',
            )
    return 0, 'Args are correct'


def get_new_sizes(height, width, result_height, result_width, scale):
    if scale:
        return math.ceil(height*scale), math.ceil(width*scale)
    if result_height and result_width:
        return result_height, result_width
    elif result_height:
        return result_height, math.ceil(width*result_height/height)
    else:
        return math.ceil(height*result_width/width), result_width


def get_result_fname(input_fname, output_fname, result_height, result_width ):
    return output_fname or '{}__{}.{}'.format(
        input_fname[:input_fname.rfind('.')],
        'x'.join(map(str, (result_height, result_width))),
        input_fname.split('.')[-1],
    )


if __name__ == '__main__':
    extensions = [
        'bmp',
        'eps',
        'gif',
        'jpg',
        'jpeg',
        'png',
        'tiff',
    ]
    args = get_args(extensions)
    exit_code, exit_text = check_args(
        args,
        extensions,
        get_file_extension,
    )
    if exit_code:
        sys.exit(exit_text)
    image = PIL.Image.open(args.fname)
    height, width = image.size
    if args.height and args.width and height/args.height != width/args.width:
        print('{} {}'.format(
            'Warning! The source and result proportions of the sides',
            'of the image do not match.',
        ))
        confirmation = input('Are you sure? [y/N]')
        if confirmation != 'y':
            sys.exit('Converting cancelled by user.')
    result_height, result_width = get_new_sizes(
        height=height,
        width=width,
        result_height=args.height,
        result_width=args.width,
        scale=args.scale,
    )
    result_fname = get_result_fname(
        input_fname=args.fname,
        output_fname=args.output,
        result_height=result_height,
        result_width=result_width,
    )
    image = PIL.Image.open(args.fname)
    try:
        image.resize((result_width, result_height)).save(result_fname)
    except (TypeError, OSError):
        print('{} from {} to {}\n{}'.format(
            'Failed to convert',
            get_file_extension(args.fname),
            get_file_extension(args.output),
            'Try to convert the image to a different format before!'
        ))
