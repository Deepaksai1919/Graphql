def apply_filters(obj, args: Optional[CompanyInput] = None):
    if args:
        if args.order_by:
            for field in args.order_by.__dict__:
                if getattr(args.order_by, field):
                    if getattr(args.order_by, field)==order.DESC:
                        obj = obj.order_by(desc(field))
                    elif getattr(args.order_by, field)==order.ASC:
                        obj = obj.order_by(field)
        if args.limit:
            obj = obj.limit(args.limit)
        if args.offset:
            obj = obj.offset(args.offset)
    print(obj)
    return obj
